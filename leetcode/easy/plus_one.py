# -*- coding:utf-8 -*-

# 66. Plus One  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = []
        digits.reverse()
        # print digits
        up = 1
        for i in digits:
            if i + up > 9:
                tmp.append(0)
                up = (i + up) / 10
            else:
                tmp.append(i + up)
                up = 0
        tmp.reverse()
        if tmp[0] == 0:
            tmp.insert(0, 1)
        return tmp


if __name__ == '__main__':
    s = Solution()
    print s.plusOne([1, 2, 3, 4, 5, 6])
    print s.plusOne([9, 9, 9, 9, 9, 9])
