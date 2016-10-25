# -*- coding:utf-8 -*-
# 112. Path Sum   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such
# that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import common.binary_tree as bt


class Solution(object):
    def get_all_path(self, root):
        """
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        for path in self.get_all_path(root.left):
            tmp = [str(root.val)]
            tmp += path
            res.append(tmp)
        for path in self.get_all_path(root.right):
            tmp = [str(root.val)]
            tmp += path
            res.append(tmp)

        return res or [str(root.val)]

    def hasPathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = self.get_all_path(root)
        for p in res:
            # print p
            if reduce(lambda x, y: int(x) + int(y), p) == sum1:
                return True

        return False


if __name__ == '__main__':
    root = bt.creat_binary_tree((5, 4, 11, 7, '*', '*', 2, '*', '*', '*', 8, 13, '*', '*', 4, '*', 1, '*', '*'))
    # bt.level_order_traver(root)
    s = Solution()
    print s.hasPathSum(root, 22)
