# -*- coding:utf-8 -*-

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

# 观察
# in  out  in  out  in  out
# 0   0    10  1    20   2
# 1   1    11  2    21   3
# 2   2    12  3
# 3   3    13  4
# 4   4    14  5
# 5   5    15  6
# 6   6    16  7
# 7   7    17  8
# 8   8    18  9
# 9   9    19  1

# (num - 1) % 10 + 1

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        rst = 0
        if num > 0:
            rst = (num - 1) % 9 + 1

        return rst


if __name__ == '__main__':
    s = Solution()
    print s.addDigits(9)
