# -*- coding:utf-8 -*-

# 111. Minimum Depth of Binary Tree   QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Contributors: Admin
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Subscribe to see which companies asked this question

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
            tmp = [root.val]
            # tmp += path
            if isinstance(path, list):
                tmp += path
            else:
                tmp.append(path)
            res.append(tmp)
        for path in self.get_all_path(root.right):
            tmp = [root.val]
            if isinstance(path, list):
                tmp += path
            else:
                tmp.append(path)
            res.append(tmp)

        return res or [root.val]

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.get_all_path(root)
        if len(res) < 1:
            return 0
        min_depth = 1 if not isinstance(res[0], list) else len(res[0])

        for i in res[1::]:
            if len(i) < min_depth:
                min_depth = len(i)

        return min_depth


if __name__ == '__main__':
    s = Solution()
    root = bt.creat_binary_tree((5, 4, 11, 7, '*', '*', 2, '*', '*', '*', 8, 13, '*', '*', 4, '*', 1, '*', '*'))
    print s.minDepth(root)
