# -*- coding:utf-8 -*-

# 169. Majority Element  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given an array of size n, find the majority element. The majority element is the element
#  that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = len(nums) / 2
        return nums[mid]


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 2, 4])
