# -*- coding:utf-8 -*-
# 9. Palindrome Number   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Subscribe to see which companies asked this question
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved
# the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
# palindrom: 回文数

import math


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not isinstance(x, int):
            return None
        if x < 0:
            return False
        p = x
        q = 0
        while p >= 10:
            q *= 10
            q += p % 10
            p /= 10

        return q == x / 10 and p == x % 10


if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(1)
    print s.isPalindrome(11)
    print s.isPalindrome(12321)
    print s.isPalindrome(2321)
    print s.isPalindrome(0)
    print s.isPalindrome(9)
    print s.isPalindrome(1111111)
    print s.isPalindrome(12345678)
    print s.isPalindrome(-2147483648)  # False
    print s.isPalindrome(1001)  # True
