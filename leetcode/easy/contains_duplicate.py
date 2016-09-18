# -*- coding:utf-8 -*-


# 217. Contains Duplicate  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
# appears at least twice in the array, and it should return false if every element is distinct.
#
# Subscribe to see which companies asked this question

import collections

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_nums = collections.Counter(nums)
        # print dict_nums

        for item in dict_nums.items():
            if item[1] > 1:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsDuplicate([1, 2, 3, 4, 4, 5, 6, 7, 8])
    print s.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8])
    print s.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9])
    print s.containsDuplicate([1, 5, -2, -4, 0])
