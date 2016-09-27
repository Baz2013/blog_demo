# -*- coding:utf-8 -*-


# 326. Power of Three  QuestionEditorial Solution  My Submissions
# Total Accepted: 65297
# Total Submissions: 169547
# Difficulty: Easy
# Given an integer, write a function to determine if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?

import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and 3 ** round(math.log(n, 3)) == n


if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfThree(9)
    print s.isPowerOfThree(10)
    print s.isPowerOfThree(27)
    print s.isPowerOfThree(99)
    print s.isPowerOfThree(243)
    # isinstance()
