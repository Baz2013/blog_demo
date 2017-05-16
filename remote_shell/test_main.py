# -*- coding:utf-8 -*-
"""
test the function in main.py
"""

import main
import unittest
import json


# {'logger_test': ['10.xx.xx.231'], 'logger': ['10.xx.xx.84:8081', '10.xx.xx.85:8081',]}
class TestMain(unittest.TestCase):
    def test_get_host(self):
        self.assertIn('10.xx.xx.231', main._get_hosts(
                {'logger_test': ['10.xx.xx.231', '10.xx.xx.232'], 'logger': ['10.xx.xx.84:8081', '10.xx.xx.85:8081']},
                'logger_test'))

    def test_get_host(self):
        self.assertIn('10.xx.xx.231', main._get_hosts(
                {'logger_test': ['10.xx.xx.231', '10.xx.xx.232'], 'logger': ['10.xx.xx.84:8081', '10.xx.xx.85:8081']},
                'logger_test'))
        self.assertIn('10.xx.xx.232', main._get_hosts(
                {'logger_test': ['10.xx.xx.231', '10.xx.xx.232'], 'logger': ['10.xx.xx.84:8081', '10.xx.xx.85:8081']},
                'logger_test'))
        self.assertIn('10.xx.xx.232', main._get_hosts(
                {'logger_test': ['10.xx.xx.231', '10.xx.xx.232'], 'logger': ['10.xx.xx.84:8081', '10.xx.xx.85:8081']},
                'logger'))
        self.assertIn('10.xx.xx.84:8081', main._get_hosts(
                {'logger_test': ['10.xx.xx.231', '10.xx.xx.232'], 'logger': ['10.xx.xx.84:8081', '10.xx.xx.85:8081']},
                'logger'))


if __name__ == '__main__':
    unittest.main()
