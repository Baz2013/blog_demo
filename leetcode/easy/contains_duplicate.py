# -*- coding:utf-8 -*-


# 217. Contains Duplicate  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
# appears at least twice in the array, and it should return false if every element is distinct.
#
# Subscribe to see which companies asked this question

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_str = ''.join([str(i) for i in nums])
        for char in num_str:
            if num_str.rfind(char) != num_str.find(char):
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsDuplicate([1, 2, 3, 4, 4, 5, 6, 7, 8])
    print s.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8])
    print s.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 9])
    print s.containsDuplicate([1, 5, -2, -4, 0])
