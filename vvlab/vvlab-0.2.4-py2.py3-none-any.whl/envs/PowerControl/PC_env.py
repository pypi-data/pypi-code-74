#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:31:50 2019
@author: farismismar
"""
import gym
import math
from gym import spaces
from gym.utils import seeding
import numpy as np
from numpy import linalg as LA
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# The GPU id to use, usually either "0" or "1";
os.environ["CUDA_VISIBLE_DEVICES"] = "0"   # My NVIDIA GTX 1080 Ti FE GPU

# An attempt to follow
# https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py

# Environment parameters
# cell radius
# UE movement speed
# BS max tx power
# BS antenna
# UE noise figure
# Center frequency
# Transmit antenna isotropic gain
# Antenna heights
# Shadow fading margin
# Number of ULA antenna elements
# Oversampling factor


class radio_environment(gym.Env):
    """In a two user two base station scenario, the SNR of the user depends on
    the channel between the user and the base station, the transmission power
    and the beamforming mode of the communication base station
    and the interference base station.

        Observation:
            Num Observation                                    Min      Max
            0   User1 server X                                 -r       r
            1   User1 server Y                                 -r       r
            2   User2 server X                                 isd-r    isd+r
            3   User2 server Y                                 -r       r
            4   Serving BS Power                               5        40W
            5   Neighbor BS power                              5        40W
            6   BF codebook index for Serving                  0        M-1
            7   BF codebook index for Neighbor                 0        M-1

    Attributes:
        M_ULA: Base station employs a uniform linear array (ULA) of M antennas.
        received_sinr_dB: SINR accepted by users.
        serving_transmit_power_dB: Transmission power of
        communication base station.
        interfering_transmit_power_dB: Transmission power of
        interfering base station.
    """

    def __init__(self, seed):

        self.M_ULA = 4
        self.cell_radius = 150  # in meters.
        self.inter_site_distance = 3*self.cell_radius / 2.
        self.num_users = 30  # number of users.
        self.gamma_0 = 5  # beamforming constant SINR.
        self.min_sinr = -3  # in dB
        self.sinr_target = self.gamma_0 + 10*np.log10(self.M_ULA)  # in dB.
        self.max_tx_power = 40  # in Watts
        self.max_tx_power_interference = 40  # in Watts
        self.f_c = 28e9  # Hz
        self.G_ant_no_beamforming = 11  # dBi
        self.prob_LOS = 0.8  # Probability of LOS transmission
        self.num_actions = 16
        self.step_count = 0  # which step

        # Where are the base stations?
        self.x_bs_1, self.y_bs_1 = 0, 0
        self.x_bs_2, self.y_bs_2 = self.inter_site_distance, 0

        # for Beamforming
        self.use_beamforming = True
        self.k_oversample = 1  # oversampling factor
        self.Np = 4  # from 3 to 5 for mmWave
        self.F = np.zeros(
            [self.M_ULA, self.k_oversample * self.M_ULA], dtype=complex)
        self.theta_n = math.pi * \
            np.arange(start=0., stop=1., step=1. /
                      (self.k_oversample*self.M_ULA))

        # Beamforming codebook F
        for n in np.arange(self.k_oversample*self.M_ULA):
            f_n = self._compute_bf_vector(self.theta_n[n])
            self.F[:, n] = f_n
        self.f_n_bs1 = None  # The index in the codebook for serving BS
        self.f_n_bs2 = None  # The index in the codebook for interfering BS

        # for Reinforcement Learning
        self.reward_min = -20
        self.reward_max = 100

        bounds_lower = np.array([
            -self.cell_radius,
            -self.cell_radius,
            self.inter_site_distance-self.cell_radius,
            -self.cell_radius,
            1,
            1,
            0,
            0])

        bounds_upper = np.array([
            self.cell_radius,
            self.cell_radius,
            self.inter_site_distance+self.cell_radius,
            self.cell_radius,
            self.max_tx_power,
            self.max_tx_power_interference,
            self.k_oversample * self.M_ULA - 1,
            self.k_oversample * self.M_ULA - 1])

        self.action_space = spaces.Discrete(
            self.num_actions)  # action size is here
        # spaces.Discrete(2) # state size is here
        self.observation_space = spaces.Box(
            bounds_lower, bounds_upper, dtype=np.float32)

        self.seed(seed=seed)

        self.state = None
#        self.steps_beyond_done = None
        self.received_sinr_dB = None
        self.serving_transmit_power_dB = None
        self.interfering_transmit_power_dB = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self, seed):
        """Reset enviornment.

        Args:
            seed: A fixed value.

        Returns:
            A fixed state.

        """
        # Initialize f_n of both cells
        self.np_random, seed = seeding.np_random(seed)
        self.f_n_bs1 = self.np_random.randint(self.M_ULA)
        self.f_n_bs2 = self.np_random.randint(self.M_ULA)

        self.state = [self.np_random.uniform(
            low=-self.cell_radius, high=self.cell_radius),
            self.np_random.uniform(
            low=-self.cell_radius, high=self.cell_radius),
            self.np_random.uniform(
            low=self.inter_site_distance-self.cell_radius,
            high=self.inter_site_distance+self.cell_radius),
            self.np_random.uniform(
            low=-self.cell_radius, high=self.cell_radius),
            self.np_random.uniform(
            low=1, high=self.max_tx_power/2),
            self.np_random.uniform(
            low=1, high=self.max_tx_power_interference/2),
            self.f_n_bs1,
            self.f_n_bs2
        ]

        self.step_count = 0

        return np.array(self.state)

    def step(self, action):
        """

        This function is used to update the environment
        after the agent outputs the action.

        Args:
            action: The action of agent.

        Returns:
            state: The state of doing an action.
            reward: Evaluate the result of an action.
            done: If the SNR, transmission power and interference power
            are within a certain range after updating
            according to a certain action, done is true.
            abort: If the SNR, transmission power and interference power
            are not within a certain range after updating
            according to a certain action, abort is true.
        """
        # assert self.action_space.contains(action),
        # "%r (%s) invalid"%(action, type(action))

        state = self.state
        reward = 0
        x_ue_1, y_ue_1, x_ue_2, y_ue_2, pt_serving, pt_interferer, \
            f_n_bs1, f_n_bs2 = state
        # based on the action make your call
        # only once a period, perform BF
        # The action is derived from a decimal interpretation
        ################################################################
        #    log_2 M (serving)    #    log_2 M (interferer)    # S # O #
        ################################################################

        if action != -1:  # optimal

            # int('0b0100101',2)
            power_command_l = action & 0b0001  # 1 power up, 0 power down
            # 1 power up, 0 power down
            power_command_b = (action & 0b0010) >> 1
            bf_selection_l = (action & 0b0100) >> 2  # 1 step up, 0 step down
            bf_selection_b = (action & 0b1000) >> 3

            self.step_count += 1
            if power_command_l == 0:
                pt_serving *= 10**(-1/10.)
            else:
                pt_serving *= 10**(1/10.)

            if power_command_b == 0:
                pt_interferer *= 10**(-1/10.)
            else:
                pt_interferer *= 10**(1/10.)

            if bf_selection_l == 1:
                f_n_bs1 = (f_n_bs1 + 1) % self.k_oversample * self.M_ULA
            else:
                f_n_bs1 = (f_n_bs1 - 1) % self.k_oversample * self.M_ULA

            if bf_selection_b == 1:
                f_n_bs2 = (f_n_bs2 + 1) % self.k_oversample * self.M_ULA
            else:
                f_n_bs2 = (f_n_bs2 - 1) % self.k_oversample * self.M_ULA

        elif action > self.num_actions - 1:
            print('WARNING: Invalid action played!')
            reward = 0
            return [], 0, False, True

        # move the UEs at a speed of v, in a random direction
        v = 2  # km/h.

        v *= 5./18  # in m/sec
        theta_1, theta_2 = self.np_random.uniform(
            low=-math.pi, high=math.pi, size=2)

        dx_1 = v * math.cos(theta_1)
        dy_1 = v * math.sin(theta_1)

        dx_2 = v * math.cos(theta_2)
        dy_2 = v * math.sin(theta_2)

        # Move UE 1
        x_ue_1 += dx_1
        y_ue_1 += dy_1

        # Move UE 2
        x_ue_2 += dx_2
        y_ue_2 += dy_2

        # Update the beamforming codebook index
        self.f_n_bs1 = f_n_bs1
        self.f_n_bs2 = f_n_bs2

        received_power, interference_power, received_sinr = self._compute_rf(
            x_ue_1, y_ue_1, pt_serving, pt_interferer, is_ue_2=False)
        received_power_ue2, interference_power_ue2, received_ue2_sinr = \
            self._compute_rf(x_ue_2, y_ue_2, pt_serving,
                             pt_interferer, is_ue_2=True)

        # keep track of quantities...
        self.received_sinr_dB = received_sinr
        self.received_ue2_sinr_dB = received_ue2_sinr
        self.serving_transmit_power_dBm = 10*np.log10(pt_serving*1e3)
        self.interfering_transmit_power_dBm = 10*np.log10(pt_interferer*1e3)

        # Did we find a FEASIBLE NON-DEGENERATE solution?
        done = all([(pt_serving <= self.max_tx_power), (pt_serving >= 0),
                    (pt_interferer <= self.max_tx_power_interference),
                    (pt_interferer >= 0), (received_sinr >= self.min_sinr),
                    (received_ue2_sinr >= self.min_sinr),
                    (received_sinr >= self.sinr_target),
                    (received_ue2_sinr >= self.sinr_target)])

        abort = any([(pt_serving > self.max_tx_power),
                     (pt_interferer > self.max_tx_power_interference),
                     (received_sinr < self.min_sinr),
                     (received_ue2_sinr < self.min_sinr),
                     (received_sinr > 70), (received_ue2_sinr > 70)])

#        print('{:.2f} dB | {:.2f} dB | {:.2f} W | {:.2f} W '.format
#        (received_sinr, received_ue2_sinr, pt_serving, pt_interferer), end='')
#        print('Done: {}'.format(done))
#        print('UE moved to ({0:0.3f},{1:0.3f})
#        and their received SINR became {2:0.3f} dB.'.format
#        (x,y,received_sinr))

        # the reward
        reward = received_sinr + received_ue2_sinr

        # Update the state.
        self.state = (x_ue_1, y_ue_1, x_ue_2, y_ue_2, pt_serving,
                      pt_interferer, f_n_bs1, f_n_bs2)

        if abort is True:
            done = False
            reward = self.reward_min
        else:
            reward += self.reward_max

#        print(done, (received_sinr >= self.sinr_target) ,
#        (pt_serving <= self.max_tx_power) ,
#        (pt_serving >= 0) , \
#        (pt_interferer <= self.max_tx_power_interference) ,
#        (pt_interferer >= 0) , (received_ue2_sinr >= self.sinr_target))

        if action == -1:        # for optimal
            return np.array(self.state), reward, False, False

        return np.array(self.state), reward, done, abort

    def _compute_bf_vector(self, theta):
        """This function corresponds to the formula in the paper (2).

        Args:
            theta: steering angle.

        Returns:
            f: Beamforming Vectors

        """
        c = 3e8  # speed of light
        wavelength = c / self.f_c

        d = wavelength / 2.  # antenna spacing
        k = 2. * math.pi / wavelength

        exponent = 1j * k * d * math.cos(theta) * np.arange(self.M_ULA)

        f = 1. / math.sqrt(self.M_ULA) * np.exp(exponent)

        # Test the norm square... is it equal to unity? YES.
        # norm_f_sq = LA.norm(f, ord=2) ** 2
        # print(norm_f_sq)

        return f

    def _compute_channel(self, x_ue, y_ue, x_bs, y_bs):
        """Random value is included in the formula, and formula test is not conducted.

        Corresponding to the formula (3) in the paper.

        Args:
        x_ue: The abscissa values of user.
        y_ue: The ordinate values of user.
        x_bs: The abscissa values of base station.
        y_bs: The ordinate values of base station.

        Returns: Channel model of downlink.

        """
        # Np is the number of paths p
        PLE_L = 2
        PLE_N = 4
        G_ant = 3  # dBi for beamforming mmWave antennas

        # Override the antenna gain if no beamforming
        if self.use_beamforming is False:
            G_ant = self.G_ant_no_beamforming

        # theta is the steering angle.  Sampled iid from unif(0,pi).
        theta = np.random.uniform(low=0, high=math.pi, size=self.Np)

        is_mmWave = (self.f_c > 25e9)
        # Calculate the transmission path loss of LOS and NLOS.
        if is_mmWave:
            path_loss_LOS = 10 ** (self._path_loss_mmWave(x_ue,
                                                          y_ue,
                                                          PLE_L,
                                                          x_bs, y_bs) / 10.)
            path_loss_NLOS = 10 ** (self._path_loss_mmWave(x_ue,
                                                           y_ue, PLE_N,
                                                           x_bs, y_bs) / 10.)
        else:
            path_loss_LOS = 10 ** (self._path_loss_sub6(x_ue,
                                                        y_ue,
                                                        x_bs, y_bs) / 10.)
            path_loss_NLOS = 10 ** (self._path_loss_sub6(x_ue,
                                                         y_ue,
                                                         x_bs, y_bs) / 10.)

        # Bernoulli for p
        alpha = np.zeros(self.Np, dtype=complex)
        p = np.random.binomial(1, self.prob_LOS)
        # 80% probability is transmitted by Los,
        # and 20% probability is transmitted by NLOS.

        # For Los transmission, the number of transmission channels is only 1.
        if p == 1:
            self.Np = 1
            alpha[0] = 1. / math.sqrt(path_loss_LOS)
        else:
            # just changed alpha to be complex in the case of NLOS
            # The NLOS gain follows Rayleigh distribution and
            # the number of transmission channels is 4.
            alpha = (np.random.normal(size=self.Np) + 1j *
                     np.random.normal(size=self.Np)) \
                / math.sqrt(path_loss_NLOS)

        rho = 1. * 10 ** (G_ant / 10.)
        # The reduction of gain loss caused by beamforming.
        # initialize the channel as a complex variable.
        h = np.zeros(self.M_ULA, dtype=complex)

        for p in np.arange(self.Np):
            a_theta = self._compute_bf_vector(theta[p])
            # scalar multiplication into a vector
            h += alpha[p] / rho * a_theta.T

        h *= math.sqrt(self.M_ULA)

#        print ('Warning: channel gain is {} dB.'.format(
#        10*np.log10(LA.norm(h, ord=2))))
        return h

    def _compute_rf(self, x_ue, y_ue, pt_bs1, pt_bs2, is_ue_2=False):
        """Random value is included in the formula, and formula test is not conducted.

        Corresponding to the formula (4) and (5) in the paper.

        Args：
        x_ue: The abscissa values of user.
        y_ue: The ordinate values of user.
        pt_bs1: Transmit power of base station 1.
        pt_bs2: Transmit power of base station 2.
        is_ue_2:
            The default is False.
            If it is True, then base station 2 is communicating with the user,
            and the signal sent by base station 1 is interference signal.
            If it is False, then base station 1 is communicating with the user,
            and the signal sent by base station 2 is interference signal.

        Returns:
        received_power: Useful power received by user.
        interference_power: Interference power received by user.
        received_sinr: User's SNR (downlink SNR).

        """

        T = 290  # Kelvins
        B = 15000  # Hz
        k_Boltzmann = 1.38e-23

        noise_power = k_Boltzmann*T*B  # this is in Watts

        if is_ue_2 is False:
            # Without loss of generality, the base station is at the origin
            # The interfering base station is x = cell_radius, y = 0
            x_bs_1, y_bs_1 = self.x_bs_1, self.y_bs_1
            x_bs_2, y_bs_2 = self.x_bs_2, self.y_bs_2

            # Now the channel h, which is a vector in beamforming.
            # This computes the channel for user
            # in serving BS from the serving BS.
            h_1 = self._compute_channel(x_ue, y_ue, x_bs=x_bs_1, y_bs=y_bs_1)
            # This computes the channel for user
            # in serving BS from the interfering BS.
            h_2 = self._compute_channel(x_ue, y_ue, x_bs=x_bs_2, y_bs=y_bs_2)

            # if this is not beamforming, there is no precoder:
            # Corresponding to the formula (4) in the paper.
            if self.use_beamforming:
                received_power = pt_bs1 * \
                    abs(np.dot(h_1.conj(), self.F[:, self.f_n_bs1])) ** 2
                interference_power = pt_bs2 * \
                    abs(np.dot(h_2.conj(), self.F[:, self.f_n_bs2])) ** 2
            else:  # the gain is ||h||^2
                received_power = pt_bs1 * LA.norm(h_1, ord=2) ** 2
                interference_power = pt_bs2 * LA.norm(h_2, ord=2) ** 2
        else:
            x_bs_1, y_bs_1 = self.x_bs_1, self.y_bs_1
            x_bs_2, y_bs_2 = self.x_bs_2, self.y_bs_2

            # Now the channel h, which is a vector in beamforming.
            # This computes the channel for user
            # in serving BS from the serving BS.
            h_1 = self._compute_channel(x_ue, y_ue, x_bs=x_bs_2, y_bs=y_bs_2)
            # This computes the channel for user
            # in serving BS from the interfering BS.
            h_2 = self._compute_channel(x_ue, y_ue, x_bs=x_bs_1, y_bs=y_bs_1)

            # if this is not beamforming, there is no precoder:
            if self.use_beamforming:
                received_power = pt_bs2 * \
                    abs(np.dot(h_1.conj(), self.F[:, self.f_n_bs2])) ** 2
                interference_power = pt_bs1 * \
                    abs(np.dot(h_2.conj(), self.F[:, self.f_n_bs1])) ** 2
            else:  # the gain is ||h||^2
                received_power = pt_bs2 * LA.norm(h_1, ord=2) ** 2
                interference_power = pt_bs1 * LA.norm(h_2, ord=2) ** 2

        # Corresponding to the formula (5) in the paper.
        interference_plus_noise_power = interference_power + noise_power
        received_sinr = 10 * \
            np.log10(received_power / interference_plus_noise_power)

        return [received_power, interference_power, received_sinr]

    # https://ieeexplore-ieee-org.ezproxy.lib.utexas.edu/stamp/stamp.jsp?tp=&arnumber=7522613
    def _path_loss_mmWave(self, x, y, PLE, x_bs=0, y_bs=0):
        """Normal distribution is included in the formula,
        and formula test is not conducted.

        Args:
        x : The abscissa values of user.
        y : The ordinate values of user.
        PLE: path loss exponent.
        x_bs: The abscissa values of base station. The default is 0.
        y_bs: The abscissa values of base station. The default is 0.

        Returns:
        L: Transmission loss of millimeter wave channel.

        """

        # These are the parameters for f = 28000 MHz.
        c = 3e8  # speed of light
        wavelength = c / self.f_c
        A = 0.0671
        Nr = self.M_ULA
        sigma_sf = 9.1
        # PLE = 3.812

        d = math.sqrt((x - x_bs)**2 + (y - y_bs)**2)  # in meters
        if d == 0:
            L = 0
        else:
            fspl = 10 * np.log10(((4*math.pi*d) / wavelength) ** 2)
            pl = fspl + 10 * np.log10(d ** PLE) * (1 - A*np.log2(Nr))

            chi_sigma = np.random.normal(0, sigma_sf)  # log-normal shadowing
            L = pl + chi_sigma

        return L  # in dB

    def _path_loss_sub6(self, x, y, x_bs=0, y_bs=0):
        """

        Args:
        x: The abscissa values of user.
        y: The ordinate values of user
        x_bs: The abscissa values of base station. The default is 0.
        y_bs: The ordinate values of base station. The default is 0.

        Returns:
        L: Transmission loss of channel.

        """
        f_c = self.f_c
        # c = 3e8  # speed of light
        d = math.sqrt((x - x_bs)**2 + (y - y_bs)**2)
        if d == 0:
            L = 0
        else:
            h_B = 20
            h_R = 1.5

    #        print('Distance from cell site is: {} km'.format(d/1000.))
            # FSPL
            # L_fspl = -10*np.log10((4.*math.pi*c/f_c / d) ** 2)

            # COST-231Hata model. It is a empirical formula.
            C = 3  # Correction factor of metropolis center
            a = (1.1 * np.log10(f_c/1e6) - 0.7) * \
                h_R - (1.56*np.log10(f_c/1e6) - 0.8)
            L_cost231 = 46.3 + 33.9 * np.log10(f_c/1e6) + 13.82 * np.log10(
                h_B) - a + (44.9 - 6.55 * np.log10(h_B)) * np.log10(
                d/1000.) + C

            L = L_cost231

        return L  # in dB
