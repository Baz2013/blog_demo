# -*- coding:utf-8 -*-
#
# 191. Number of 1 Bits  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has
# (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
# so the function should return 3.

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return
        tmp = bin(n)
        binary_str = tmp[2::]
        # print binary_str
        gen = (int(x) for x in binary_str)
        return sum(gen)




if __name__ == '__main__':
    s = Solution()
    print s.hammingWeight(32)
    print s.hammingWeight(7)
    print s.hammingWeight(8)