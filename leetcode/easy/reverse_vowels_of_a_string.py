# -*- coding:utf-8 -*-

# 345. Reverse Vowels of a String  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".

import time


class Solution(object):
    def reverseVowels_1(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        tmp_lst = list()
        for c in s:
            if c in vowels:
                tmp_lst.append(c)
        tmp_lst.reverse()
        # print tmp_lst

        new_s = list()
        i = 0
        for c in s:
            if c in vowels:
                new_s.append(tmp_lst[i])
                i += 1
            else:
                new_s.append(c)

        return ''.join(new_s)

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        j = 0
        k = len(s) - 1
        tmp_lst = list(s)
        while j < k:
            while tmp_lst[j] not in vowels and j < k:
                j += 1
            while tmp_lst[k] not in vowels and j < k:
                k -= 1
            tmp_lst[j], tmp_lst[k] = tmp_lst[k], tmp_lst[j]
            j += 1
            k -= 1

        return ''.join(tmp_lst)


if __name__ == '__main__':
    s = Solution()
    print s.reverseVowels("hello")
    print s.reverseVowels("leetcode")
    print s.reverseVowels_1("leetcode")
    print s.reverseVowels_1("hello")
    print s.reverseVowels_1("")
    print s.reverseVowels_1("aA")
