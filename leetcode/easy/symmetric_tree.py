# -*- coding:utf-8 -*-

# 101. Symmetric Tree  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# pre: [1,2,3,'*','*',4,'*','*',2,4,'*','*',3'*','*']
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# pre: [1,2,'*',3,'*','*',2,'*',3,'*','*']
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import common.binary_tree as bt


class Solution(object):
    def symmetric(self, left, right):
        """
        :param left:
        :param right:
        :return:
        """
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val and self.symmetric(left.left, right.right) and self.symmetric(left.right,
                                                                                                   right.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtyp bool
        """
        if not root:
            return True

        return self.symmetric(root.left, root.right)

    def isSymmetric_1(self, root):
        """
        非递归方法
        :param root:
        :return:
        """
        if not root:
            return True

        stack = list()
        import Queue
        queue = Queue.Queue()

        queue.put(root)
        while queue.qsize() > 0:
            print stack
            node = queue.get()
            if len(stack) > 0:
                if stack[-1] == node.val:
                    stack.pop()
                else:
                    stack.append(node.val)
            else:
                stack.append(node.val)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

        return True if len(stack) == 1 else False


if __name__ == '__main__':
    s = Solution()
    # root = bt.creat_binary_tree([1, 2, 3, '*', '*', 4, '*', '*', 2, 4, '*', '*', 3, '*', '*'])
    root1 = bt.creat_binary_tree([1, 2, '*', 3, '*', '*', 2, '*', 3, '*', '*'])
    # bt.level_order_traver(root)
    print s.isSymmetric(root1)
    print s.isSymmetric_1(root1)
