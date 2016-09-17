# -*- coding:utf-8 -*-

# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        max_left = 1 + self.maxDepth(root.left)
        max_right = 1 + self.maxDepth(root.right)

        return max(max_left, max_right)


if __name__ == '__main__':
    bt = TreeNode(1)
    bt.left = TreeNode(2)
    bt.right = TreeNode(3)
    bt.right.right = TreeNode(5)

    s = Solution()
    print s.maxDepth(bt)
