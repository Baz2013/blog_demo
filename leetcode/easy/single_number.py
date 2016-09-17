# -*- coding:utf-8 -*-

# Given an array of integers, every element appears twice except for one. Find that single one.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# 1. 相同的整数异或等于0 2.异或满足交换律

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        for i in nums:
            rst = rst ^ i

        return rst


if __name__ == '__main__':
    num_lst = [1, 2, 2, 3, 1, 3, 5, 5, 6, 8, 9, 8, 9]
    s = Solution()
    print s.singleNumber(num_lst)
