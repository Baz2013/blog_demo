# -*- coding:utf-8 -*-

# 405. Convert a Number to Hexadecimal  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer,
# two’s complement method is used.
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero,
# it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal
#  string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        letters = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
        ret = ''
        if num == 0:
            return '0'
        if num < 0:
            num += 2 ** 32

        while num > 0:
            num, val = divmod(num, 16)
            ret += letters[val]

        return ret[::-1]

    def toHex_1(self, num):
        """
        :type num: int
        :rtype: str
        """
        letters = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
        ret = ''
        if num == 0:
            return '0'
        if num < 0:
            num += 2 ** 32

        while num != 0:
            ret = letters[num & 15] + ret
            num >>= 4

        return ret


if __name__ == '__main__':
    s = Solution()
    print s.toHex_1(26)
    print s.toHex_1(-1)
