# -*- coding:utf-8 -*-

# 242. Valid Anagram  QuestionEditorial Solution  My Submissions
# Total Accepted: 109499
# Total Submissions: 250233
# Difficulty: Easy
# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# 如果只是顺序边了,而字符没有变是合法的

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lst_s, lst_t = list(s), list(t)
        lst_s.sort()
        lst_t.sort()

        return False if ''.join(lst_s) != ''.join(lst_t) else True


if __name__ == '__main__':
    s = Solution()
    print s.isAnagram("anagram", "nagaram")
    print s.isAnagram("rat", "car")
