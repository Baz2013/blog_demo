# -*- coding:utf-8 -*-
#
# 102. Binary Tree Level Order Traversal  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
import common.binary_tree as bt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import Queue
        if not root:
            return []
        tmp = list()
        queue = Queue.Queue()
        queue.put(root)
        while queue.qsize() != 0:
            level = []
            len = queue.qsize()
            for i in range(len):
                front = queue.get()
                level.append(front.val)
                if front.left:
                    queue.put(front.left)
                if front.right:
                    queue.put(front.right)

            tmp.append(level)
        return tmp

if __name__ == '__main__':
    root = bt.creat_binary_tree([3, 9, '*', '*', 20, 15, '*', '*', 7, '*', '*'])
    s = Solution()
    print s.levelOrder(root)