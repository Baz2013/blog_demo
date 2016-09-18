# -*- coding:utf-8 -*-

# 171. Excel Sheet Column Number  QuestionEditorial Solution  My Submissions
# Total Accepted: 98887
# Total Submissions: 224926
# Difficulty: Easy
# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
import math


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        # char_lst = list(s)
        # if len(char_lst) == 1:
        #     sum = ord(char_lst[0]) - 64
        # elif len(char_lst) == 2:
        #     sum = ord(char_lst[1]) - 64 + (ord(char_lst[0]) - 64) * 26
        # elif len(char_lst) == 3:
        #     sum = ord(char_lst[2]) - 64 + (ord(char_lst[1]) - 64) * 26 + (ord(char_lst[0]) - 64) * 26 * 26
        # else:
        #     return
        ch_lst = list(s)
        for index, ch in enumerate(ch_lst[::-1]):
            sum += (ord(ch) - 64) * math.pow(26, index)

        return int(sum)


if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber('B')
    print s.titleToNumber('Z')
    print s.titleToNumber('AA')
    print s.titleToNumber('AB')
    print s.titleToNumber('AC')
    print s.titleToNumber('AZ')
    print s.titleToNumber('BA')
    print s.titleToNumber('BZ')
    print s.titleToNumber('AAA')
