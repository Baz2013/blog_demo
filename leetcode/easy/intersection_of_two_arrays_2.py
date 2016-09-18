# -*- coding:utf-8 -*-

# 350. Intersection of Two Arrays II  QuestionEditorial Solution  My Submissions
# Total Accepted: 33012
# Total Submissions: 77712
# Difficulty: Easy
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot
# load all elements into the memory at once?
# Subscribe to see which companies asked this question

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter_set = set(nums1) & set(nums2)
        rst_lst = list()

        for c in inter_set:
            for i in range(min(nums1.count(c), nums2.count(c))):
                rst_lst.append(c)

        return rst_lst


if __name__ == '__main__':
    s = Solution()
    print s.intersect([1, 2, 2, 1], [2, 2, 2])
    print s.intersect([1, 1], [2])
    print s.intersect([1, 1], [1])