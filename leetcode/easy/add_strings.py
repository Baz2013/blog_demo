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
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0:
            x = 0 if i < 0 else int(num1[i])
            y = 0 if j < 0 else int(num2[j])
            res.append((x + y + carry) % 10)
            carry = (x + y + carry) / 10
            i -= 1
            j -= 1

        if carry > 0:
            res.append(carry)

        res.reverse()
        return ''.join([str(i) for i in res])


if __name__ == '__main__':
    s = Solution()
    print s.addStrings('123', '456')
    print s.addStrings('1', '456')
    print s.addStrings('999999999999999999', '1')
