import unittest

from smartconfigparser import smartconfigparser


class TestCaseSmartConfigParser(unittest.TestCase):
    def setUp(self):
        self.config = smartconfigparser.Config()
        self.config.read('config.ini')

    def test_get_value(self):
        self.assertEqual('test_user', self.config.get('database', 'user'))

    def test_get_value_case_insensitive(self):
        self.assertEqual('test_user', self.config.get('database', 'uSEr'))

    def test_getfloat_value(self):
        self.assertEqual(125.12, self.config.getfloat('default', 'float'))

    def test_getint_value(self):
        self.assertEqual(12, self.config.getint('default', 'int'))

    def test_getboolean_value(self):
        self.assertEqual(True, self.config.getboolean('default', 'boolean'))

    def test_get_default_value(self):
        self.assertEqual('default value', self.config.get('section_does_not_exist', 'user', 'default value'))


if __name__ == '__main__':
    unittest.main()
