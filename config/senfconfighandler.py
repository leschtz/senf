from .senfconfig import SenfConfig


class SenfConfigHandler(object):
    def __init__(self, config_file=None):
        self.config_file = config_file
        pass

    def setup(self):
        senf_config_handler = SenfConfig(self.config_file)
        return senf_config_handler
