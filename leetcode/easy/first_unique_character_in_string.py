# -*- coding:utf-8 -*-

# 387. First Unique Character in a String  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, c in enumerate(s):
            if s.rfind(c) == s.find(c):
                return i

        return -1


if __name__ == '__main__':
    s = Solution()
    print s.firstUniqChar('leetcode')
    print s.firstUniqChar('loveleetcode')
    print s.firstUniqChar('aassbccb')
