#!/usr/bin/env python3

from btcpy.structs.sig import (
    P2pkhSolver, IfElseSolver
)

import json
import os

from swap.providers.bitcoin.solver import (
    NormalSolver, FundSolver, ClaimSolver, RefundSolver
)

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "..", "values.json"))
values = open(file_path, "r")
_ = json.loads(values.read())
values.close()


def test_bitcoin_normal_solver():

    normal_solver = NormalSolver(
        root_xprivate_key=_["bitcoin"]["wallet"]["sender"]["root_xprivate_key"],
        path=_["bitcoin"]["wallet"]["sender"]["derivation"]["path"],
        account=_["bitcoin"]["wallet"]["sender"]["derivation"]["account"],
        change=_["bitcoin"]["wallet"]["sender"]["derivation"]["change"],
        address=_["bitcoin"]["wallet"]["sender"]["derivation"]["address"]
    )

    assert isinstance(normal_solver.solve(network=_["bitcoin"]["network"]), P2pkhSolver)


def test_bitcoin_fund_solver():

    fund_solver = FundSolver(
        root_xprivate_key=_["bitcoin"]["wallet"]["sender"]["root_xprivate_key"],
        path=_["bitcoin"]["wallet"]["sender"]["derivation"]["path"],
        account=_["bitcoin"]["wallet"]["sender"]["derivation"]["account"],
        change=_["bitcoin"]["wallet"]["sender"]["derivation"]["change"],
        address=_["bitcoin"]["wallet"]["sender"]["derivation"]["address"]
    )

    assert isinstance(fund_solver.solve(network=_["bitcoin"]["network"]), P2pkhSolver)


def test_bitcoin_claim_solver():

    claim_solver = ClaimSolver(
        root_xprivate_key=_["bitcoin"]["wallet"]["recipient"]["root_xprivate_key"],
        secret_key=_["bitcoin"]["htlc"]["secret"]["key"],
        bytecode=_["bitcoin"]["htlc"]["bytecode"],
        path=_["bitcoin"]["wallet"]["recipient"]["derivation"]["path"],
        account=_["bitcoin"]["wallet"]["recipient"]["derivation"]["account"],
        change=_["bitcoin"]["wallet"]["recipient"]["derivation"]["change"],
        address=_["bitcoin"]["wallet"]["recipient"]["derivation"]["address"]
    )

    assert isinstance(claim_solver.solve(network=_["bitcoin"]["network"]), IfElseSolver)


def test_bitcoin_refund_solver():

    refund_solver = RefundSolver(
        root_xprivate_key=_["bitcoin"]["wallet"]["sender"]["root_xprivate_key"],
        bytecode=_["bitcoin"]["htlc"]["bytecode"],
        sequence=_["bitcoin"]["htlc"]["sequence"],
        path=_["bitcoin"]["wallet"]["sender"]["derivation"]["path"],
        account=_["bitcoin"]["wallet"]["sender"]["derivation"]["account"],
        change=_["bitcoin"]["wallet"]["sender"]["derivation"]["change"],
        address=_["bitcoin"]["wallet"]["sender"]["derivation"]["address"]
    )

    assert isinstance(refund_solver.solve(network=_["bitcoin"]["network"]), IfElseSolver)
