# -*- coding:utf-8 -*-

# 389. Find the Difference
# Difficulty: Easy
# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Find the letter that was added in t.

# 类比 single number题目

import collections
print collections.Counter('abc')

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds = collections.Counter(s)
        dt = collections.Counter(t)

        return (dt - ds).keys().pop()

    def findTheDifference_1(self, s, t):
        """
        :param s:
        :param t:
        :return:
        """

        rst = 0
        for x in s + t:
            rst = rst ^ ord(x)

        return chr(rst)


if __name__ == '__main__':
    s = Solution()
    print s.findTheDifference('abcd', 'abcde')  # e
    print s.findTheDifference('abc', 'adcb')

    print s.findTheDifference_1('abcd', 'abcde')  # e
    print s.findTheDifference_1('abc', 'adcb')