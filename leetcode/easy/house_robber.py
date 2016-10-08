# -*- coding:utf-8 -*-

# 198. House Robber
# Difficulty: Easy
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
#  the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
# 动态规划问题

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            # print 'last = %d,now = %d, i = %d' % (last, now, i)
            last, now = now, max(last + i, now)

        return now


if __name__ == '__main__':
    s = Solution()
    print s.rob([1, 2, 3, 4, 5, 6])
    print '-' * 20
    print s.rob([1, 2, 3, 4, 99, 6])
    print '-' * 20
    print s.rob([1, 1, 1, 98, 99, 1])
