import os
import tempfile
import unittest

from smartconfigparser import Config


class TestCaseSmartConfigParser(unittest.TestCase):
    def setUp(self):
        self.config = Config()
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

    def test_set_default_value(self):
        self.config.set('section_does_not_exist', 'user', 'Guillaume Vincent')
        temp_file = tempfile.NamedTemporaryFile(suffix='.ini', dir=os.path.dirname(__file__))
        with open(temp_file.name, 'wt') as configfile:
            self.config.write(configfile)

        with open(temp_file.name) as f: content = f.read()
        self.assertTrue("user = Guillaume Vincent" in content)

    def test_getlist(self):
        self.assertEqual(['list', 'of', ' string'], self.config.getlist('default', 'list'))

    def test_getlist_get_default_value(self):
        self.assertEqual(['a', 'b', 'c'], self.config.getlist('section_does_not_exist', 'list', ['a', 'b', 'c']))


if __name__ == '__main__':
    unittest.main()
