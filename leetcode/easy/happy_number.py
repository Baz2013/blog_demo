# -*- coding:utf-8 -*-

# 202. Happy Number  QuestionEditorial Solution  My Submissions
# Total Accepted: 89693
# Total Submissions: 234678
# Difficulty: Easy
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
#  replace the number by the sum of the squares of its digits, and repeat the process until the number
# equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers
# for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number

# this looks more similar to Linked List Cycle
# 使用快慢指针判断

class Solution(object):
    def next_number(self, n):
        """
        :param n:
        :return:
        """
        rst = list()
        while n > 9:
            t = n % 10
            rst.append(t)
            n /= 10

        rst.append(n)

        return sum([x ** 2 for x in rst])

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = self.next_number(n)

        while slow != fast:
            slow = self.next_number(slow)
            fast = self.next_number(self.next_number(fast))

        return 1 == slow


if __name__ == '__main__':
    s = Solution()
    print s.isHappy(19)
    print s.isHappy(1111111)
    print s.isHappy(77777)
    print s.isHappy(9999)
