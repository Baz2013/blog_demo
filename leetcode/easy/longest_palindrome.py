# -*- coding:utf-8 -*-

# 409. Longest Palindrome   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res_dict = {}
        for c in s:
            if res_dict.get(c, False):
                res_dict[c] += 1
            else:
                res_dict[c] = 1

        odd_flag = 0
        for item in res_dict.items():
            odd_flag += item[1] % 2

        if odd_flag > 0:
            return len(s) - odd_flag + 1
        else:
            return len(s)


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome('abccccdd')
    print s.longestPalindrome('a')
    print s.longestPalindrome('ab')
    print s.longestPalindrome('abcd')
    print s.longestPalindrome('abcdc')
