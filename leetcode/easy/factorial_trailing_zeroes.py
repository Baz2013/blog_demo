# -*- coding:utf-8 -*-
# 172. Factorial Trailing Zeroes  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
# 10 = 2 * 5
# example: 11! = 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 可以看出2的个数比5的个数多,所以只需要求出5的个数就是0的个数
# from http://www.purplemath.com/modules/factzero.htm

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += n / 5
            n /= 5

        return res

    def trailingZeroes_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        x = 5
        while n >= x:
            res += n / x
            x *= 5

        return res


if __name__ == '__main__':
    s = Solution()
    print s.trailingZeroes(1)
    print s.trailingZeroes(6)
    print s.trailingZeroes(11)
    print s.trailingZeroes(101)
    print s.trailingZeroes(1001)
    print s.trailingZeroes(4617)
    print s.trailingZeroes_1(4617)
