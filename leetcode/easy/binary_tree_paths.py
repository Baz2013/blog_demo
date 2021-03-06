# -*- coding:utf-8 -*-

# 257. Binary Tree Paths   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import common.binary_tree as bt


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        """
        :param root:
        :return:
        """
        if not root:
            return []
        res = [str(root.val) + "->" + path for path in self.binaryTreePaths(root.left)]
        res += [str(root.val) + "->" + path for path in self.binaryTreePaths(root.right)]

        return res or [str(root.val)]


if __name__ == '__main__':
    # root = bt.creat_binary_tree([1, 2, '*', 5, '*', '*', 3, '*', '*'])
    root = bt.creat_binary_tree([6, 2, 0, '*', '*', 4, 3, '*', '*', 5, '*', '*', 8, 7, '*', '*', 9, '*', '*'])
    # bt.level_order_traver(root)
    # print
    # bt.after_order_travel(root)
    s = Solution()
    print s.binaryTreePaths(root)
