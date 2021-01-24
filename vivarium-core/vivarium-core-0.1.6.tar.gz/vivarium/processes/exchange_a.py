from vivarium.core.process import Process


class ExchangeA(Process):
    """ Exchange A

    A minimal exchange process that moves molecules 'A' between internal
    and external ports
    """
    name = 'exchange_a'
    defaults = {
        'uptake_rate': 0.0,
        'secrete_rate': 0.0}

    def __init__(self, parameters=None):
        super(ExchangeA, self).__init__(parameters)
        self.uptake_rate = self.parameters['uptake_rate']
        self.secrete_rate = self.parameters['secrete_rate']

    def ports_schema(self):
        return {
            'internal': {
                'A': {
                    '_default': 0.0,
                    '_emit': True}},
            'external': {
                'A': {
                    '_default': 0.0,
                    '_emit': True}}}

    def next_update(self, timestep, states):
        a_in = states['internal']['A']
        a_out = states['external']['A']
        delta_a_in = a_out * self.uptake_rate - a_in * self.secrete_rate
        return {
            'internal': {'A': delta_a_in},
            'external': {'A': -delta_a_in}}
