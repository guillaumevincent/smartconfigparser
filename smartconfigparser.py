try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser


class Config(ConfigParser):
    def get(self, section, option, default=None, *args, **kwargs):
        if self.has_option(section, option) or default is None:
            return ConfigParser.get(self, section, option)
        else:
            return default

    def getint(self, section, option, default=None, *args, **kwargs):
        if self.has_option(section, option) or not isinstance(default, int):
            return ConfigParser.getint(self, section, option)
        else:
            return default

    def getfloat(self, section, option, default=None, *args, **kwargs):
        if self.has_option(section, option) or not isinstance(default, float):
            return ConfigParser.getfloat(self, section, option)
        else:
            return default

    def getboolean(self, section, option, default=None, *args, **kwargs):
        if self.has_option(section, option) or not isinstance(default, bool):
            return ConfigParser.getboolean(self, section, option)
        else:
            return default