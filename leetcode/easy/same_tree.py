# -*- coding:utf-8 -*-

# 100. Same Tree  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# 结构和数据相同

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if (p is not None and q is None) or (p is None and q is not None):
            return False

        if p.val != q.val :
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    s = Solution()
    # s.isSameTree()
