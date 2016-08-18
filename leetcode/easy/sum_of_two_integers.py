# -*- coding:utf-8 -*-
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# Given a = 1 and b = 2, return 3.

import time
import ctypes


# http://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
# https://en.wikipedia.org/wiki/Adder_%28electronics%29#Half_adder
# http://stackoverflow.com/questions/30696484/a-b-without-arithmetic-operators-python-vs-c

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a = ctypes.c_int32(a).value
        b = ctypes.c_int32(b).value

        while b != 0:
            print "-----------%d" % (b,)
            time.sleep(1)
            tmp = ctypes.c_int32(a & b).value
            a = ctypes.c_int32(a ^ b).value
            b = ctypes.c_int32(tmp << 1).value

        return a


solution = Solution()
# print solution.getSum(1, 2)
# print solution.getSum(32, 15)
# print solution.getSum(999999999999999, 111111111111111)
print solution.getSum(-1, 2)
