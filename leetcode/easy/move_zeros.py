# -*-coding:utf-8 -*-


# 283. Move Zeroes  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)
        k = 0
        for i in nums:
            if 0 != i:
                nums[k] = i
                k += 1
        for i in range(1, cnt + 1):
            nums[-i] = 0


if __name__ == '__main__':
    s = Solution()
    lst = [0, 1, 0, 3, 12]
    s.moveZeroes(lst)
    print lst
