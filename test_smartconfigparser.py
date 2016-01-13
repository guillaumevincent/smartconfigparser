import os
import tempfile
import unittest
import uuid

from smartconfigparser import Config


class SmartConfigParserTestCases(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.config.read('config.ini')
        self.unknown_section = str(uuid.uuid4())

    def test_get_default_if_section_does_not_exist(self):
        self.assertEqual('guillaume', self.config.get(self.unknown_section, 'user', 'guillaume'))

    def test_get_value(self):
        self.assertEqual('test_user', self.config.get('database', 'user'))

    def test_get_value_case_insensitive(self):
        self.assertEqual('test_user', self.config.get('database', 'uSEr'))

    def test_getfloat_value(self):
        self.assertEqual(125.12, self.config.getfloat('default', 'float'))

    def test_getfloat_default_value(self):
        self.assertEqual(123.34, self.config.getfloat(self.unknown_section, 'float', 123.34))

    def test_getfloat_default_value_raises_error_if_not_a_float(self):
        with self.assertRaises(Exception) as context:
            self.config.getfloat(self.unknown_section, 'float', '123.34')

    def test_getint_value(self):
        self.assertEqual(12, self.config.getint('default', 'int'))

    def test_getint_default_value(self):
        self.assertEqual(13, self.config.getint(self.unknown_section, 'int', 13))

    def test_getint_default_value_raises_error_if_not_an_int(self):
        with self.assertRaises(Exception) as context:
            self.config.getint(self.unknown_section, 'int', '12')

    def test_getboolean_value(self):
        self.assertTrue(self.config.getboolean('default', 'boolean'))

    def test_getboolean_default_value(self):
        self.assertFalse(self.config.getboolean(self.unknown_section, 'boolean', False))

    def test_getboolean_default_value_raises_error_if_not_an_boolean(self):
        with self.assertRaises(Exception) as context:
            self.config.getboolean(self.unknown_section, 'boolean', 'False')

    def test_set_default_value(self):
        self.config.set(self.unknown_section, 'user', 'Guillaume Vincent')
        temp_file = tempfile.NamedTemporaryFile(suffix='.ini', dir=os.path.dirname(__file__))
        with open(temp_file.name, 'wt') as configfile:
            self.config.write(configfile)

        with open(temp_file.name) as f: content = f.read()
        self.assertTrue("user = Guillaume Vincent" in content)

    def test_getlist(self):
        self.assertEqual(['list', 'of', ' string'], self.config.getlist('default', 'list'))

    def test_getlist_get_default_value(self):
        self.assertEqual(['a', 'b', 'c'], self.config.getlist(self.unknown_section, 'list', ['a', 'b', 'c']))

    def test_unicode_char(self):
        self.assertEqual('%s', self.config.get('raw', 'percent_s'))


if __name__ == '__main__':
    unittest.main()
