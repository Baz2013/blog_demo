# -*- coding:utf-8 -*-

# 110. Balanced Binary Tree  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the
# depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import common.binary_tree as bt


class Solution(object):
    def depth(self, root):
        """
        :param root:
        :return:
        """
        if not root:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        return 1 + (left_depth if left_depth > right_depth else right_depth)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        l_depth = self.depth(root.left)
        r_depth = self.depth(root.right)

        if abs(l_depth - r_depth) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    root = bt.creat_binary_tree([6, 2, 0, '*', '*', 4, 3, '*', '*', 5, '*', '*', 8, 7, '*', '*', 9, '*', '*'])
    # root = bt.creat_binary_tree([1, 2, 4, 6, '*', '*', '*', 5, '*', '*', 3, '*', '*'])
    s = Solution()
    print s.depth(root)
    print s.isBalanced(root)
