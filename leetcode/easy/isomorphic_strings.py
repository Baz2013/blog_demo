# -*- coding:utf-8 -*-

import unittest


# 205. Isomorphic Strings   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the
# order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dict_s, dict_t = dict(), dict()

        for i in range(len(s)):
            source, target = dict_s.get(t[i]), dict_t.get(s[i])
            if source is None and target is None:
                dict_s[t[i]], dict_t[s[i]] = s[i], t[i]
            elif source != s[i] or target != t[i]:
                return False

        return True


class solutionTest(unittest.TestCase):
    def test_isIsomorphic(self):
        s = Solution()
        self.assertEquals(False, s.isIsomorphic('foo', 'bar'))
        self.assertEquals(True, s.isIsomorphic('foo', 'add'))
        self.assertEquals(True, s.isIsomorphic('paper', 'title'))
        self.assertEquals(True, s.isIsomorphic('pa', 'title'))
