import configparser


class SenfConfig(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.default_section = None
        pass

    def read_config_file(self):
        self.config.read(self.config_file)

    def get_default_study(self):
        for section_name in self.config.sections():
            section = self.config[section_name]
            if section.getboolean('default') is True:
                self.default_section = self.config[section_name]
                return section_name

    def get_section(self, section='DEFAULT'):
        for key in self.config[section]:
            print(key)

    def get_study(self, section=None):
        return self.__get_key_value(section, 'study')

    def get_path(self, section=None):
        return self.__get_key_value(section, 'path')

    def __get_key_value(self, section=None, key=None):
        section = section if section is not None else self.default_section

        if not key:
            return

        return section[key]
