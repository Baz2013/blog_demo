# -*- coding:utf-8 -*-

# 70. Climbing Stairs
# Difficulty: Easy
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Subscribe to see which companies asked this question
# 先枚举下,发现符合斐波那契数列
# 1 1
# 2 2
# 3 3
# 4 5
# 5 8
# 在用递归的方法算较大的斐波那契数的时候,由于递归栈太深,并且大部分都是重复的运算,导致耗时较长
# 所以需要用非递归的方式解此题
# 参考:http://www.cnblogs.com/python27/archive/2011/11/25/2261980.html

class Solution(object):
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 1 == n:
            return 1
        elif 2 == n:
            return 2

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if 1 == n:
            return 1

        first_val = 0
        second_val = 1
        fib = 0
        cnt = 1
        while cnt < n + 1:
            fib = first_val + second_val
            first_val = second_val
            second_val = fib
            cnt += 1

        return fib

if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(2)
    print s.climbStairs(4)
    print s.climbStairs(10)
    print s.climbStairs(35)
    print s.climbStairs1(35)