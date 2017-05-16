# -*- coding:utf-8 -*-
"""
test the function in utils.py
"""

import unittest
import utils


class TestMain(unittest.TestCase):
    def test_split_copy_command(self):
        self.assertIn('/abc/123/a.txt', utils.split_copy_command('src = /abc/123/a.txt dest=/def/user/'))
        self.assertIn('/def/user/', utils.split_copy_command('src = /abc/123/a.txt dest=/def/user/'))
        self.assertNotIn('src', utils.split_copy_command('src = /abc/123/a.txt dest=/def/user/'))

if __name__ == '__main__':
    unittest.main()