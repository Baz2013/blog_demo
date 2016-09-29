# -*- coding:utf-8 -*-

# 404. Sum of Left Leaves  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import common.binary_tree as bt


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        if root.left and not root.left.left and not root.left.right:
            sum += root.left.val

        return sum

    def sumOfLeftLeaves_1(self, root):
        """
        使用迭代的方法
        :type root: TreeNode
        :rtype: int
        """
        
        return sum


if __name__ == '__main__':
    # root = bt.creat_binary_tree([1, 2, 4, 6, '*', '*', '*', 5, '*', '*', 3, '*', '*'])
    # root = bt.creat_binary_tree([1, 2, 4, '*', '*', 5, '*', '*', 3, '*', '*'])
    root = bt.creat_binary_tree([3, 9, '*', '*', 20, 15, '*', '*', 7, '*', '*'])
    # bt.level_order_traver(root)
    s = Solution()
    print s.sumOfLeftLeaves(root)
