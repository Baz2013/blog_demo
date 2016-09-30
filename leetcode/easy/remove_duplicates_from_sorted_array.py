# -*- coding:utf-8 -*-

# 26. Remove Duplicates from Sorted Array  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a sorted array, remove the duplicates in place such that each element appear only once and
# return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#  It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = list()
        if len(nums) <= 1:
            return len(nums)
        p = 0
        q = 1
        l = len(nums)
        while q < l:
            if nums[p] == nums[q]:
                nums.pop(q)
                l -= 1
            else:
                p += 1
                q += 1
        # print nums

        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1, 1, 2])
    print s.removeDuplicates([1, 1, 1, 1, 1, 1, 1])
    print s.removeDuplicates([1, 2, 3, 4, 5, 6, 7])
    print s.removeDuplicates([1, 2, 2, 2, 2, 2, 2, 2])
