import unittest

from peewee import SqliteDatabase
from selenium import webdriver

from Environment import env, env_driver, get_database


class ConfigLoaderEnvironmentTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_env_with_undefined_key(self):
        self.assertRaises(KeyError, env, 'DUR')

    def test_env_with_defined_key(self):
        self.assertEqual(env('BROWSER'), 'chrome')

    def test_env_driver_with_defined_browser(self):
        self.assertEqual(env_driver(env('BROWSER')), webdriver.Chrome)

    def test_env_driver_with_undefined_browser(self):
        self.assertEqual(env_driver(env('DB')), False)

    def test_get_database_with_defined_database_type(self):
        self.assertIsInstance(get_database(env('DB_TYPE')), SqliteDatabase)

    def test_get_database_with_undefined_database_type(self):
        self.assertEqual(get_database(env('BROWSER')), False)

    def test_get_list(self):
        self.assertIsInstance(env('LIST'), list)

    def test_get_dict(self):
        self.assertIsInstance(env('DICT'), dict)

    def test_list_values(self):
        self.assertEqual(env('LIST')[0], 'Item1')
        self.assertEqual(env('LIST')[1], 'Item2')

    def test_dict_values(self):
        self.assertEqual(env('DICT')['key1'], 'value1')
        self.assertEqual(env('DICT')['key2'], 'value2')

    def test_empty_list(self):
        self.assertEqual(env('EMPTY_LIST'), [])

    def test_empty_dict(self):
        self.assertEqual(env('EMPTY_DICT'), {})

    def tearDown(self):
        pass


def main():
    unittest.main()

if __name__ == '__main__':
    main()
