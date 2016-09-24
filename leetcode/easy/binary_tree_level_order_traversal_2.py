# -*- coding:utf-8 -*-

# 107. Binary Tree Level Order Traversal II  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

import common.binary_tree as bt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

if __name__ == '__main__':
    s = Solution()
    root = bt.creat_binary_tree([3, 9, '*', '*', 20, 15, '*', '*', 7, '*', '*'])
    # bt.pre_order_travel(root)
    # print
    # bt.mid_order_travel(root)
