# -*- coding:utf-8 -*-
#
# 415. Add Strings   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        if len1 > len2:
            while


if __name__ == '__main__':
    s = Solution()
    s.addStrings('123', '456')
