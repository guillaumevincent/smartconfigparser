try:
    from ConfigParser import RawConfigParser
except ImportError:
    from configparser import RawConfigParser


class Config(RawConfigParser):
    def get(self, section, option, default=None, *args, **kwargs):
        if self.has_option(section, option) or default is None:
            return RawConfigParser.get(self, section, option)
        else:
            return default

    def getint(self, section, option, default=None, *args, **kwargs):
        if self.has_option(section, option) or not isinstance(default, int):
            return RawConfigParser.getint(self, section, option)
        else:
            return default

    def getfloat(self, section, option, default=None, *args, **kwargs):
        if self.has_option(section, option) or not isinstance(default, float):
            return RawConfigParser.getfloat(self, section, option)
        else:
            return default

    def getboolean(self, section, option, default=None, *args, **kwargs):
        if self.has_option(section, option) or not isinstance(default, bool):
            return RawConfigParser.getboolean(self, section, option)
        else:
            return default

    def set(self, section, option, value=None):
        if not self.has_section(section):
            self.add_section(section)
        RawConfigParser.set(self, section, option, value)

    def getlist(self, section, option, default=None):
        if self.has_option(section, option) or default is None:
            return RawConfigParser.get(self, section, option).split(',')
        else:
            return default
