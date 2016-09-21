# -*- coding:utf-8 -*-
# BST: Binary Search Tree
#
# 235. Lowest Common Ancestor of a Binary Search Tree  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
#  two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow
# a node to be a descendant of itself).”
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of
# nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# 二叉查找树（Binary Search Tree），或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，
# 则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
# 它的左、右子树也分别为二叉排序树

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import common.binary_tree as bt


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        if root.val == p.val or q.val == root.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None

    def lowestCommonAncestor_1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        from : https://discuss.leetcode.com/topic/18387/3-lines-with-o-1-space-1-liners-alternatives
        """
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]

        return root


if __name__ == '__main__':
    s = Solution()
    head = bt.creat_binary_tree([6, 2, 0, '*', '*', 4, 3, '*', '*', 5, '*', '*', 8, 7, '*', '*', 9, '*', '*'])
    # bt.pre_order_travel(head)
    node1 = bt.TreeNode(2)
    node2 = bt.TreeNode(8)
    ancestor = s.lowestCommonAncestor(head, node1, node2)
    print ancestor.val

    ancestor = s.lowestCommonAncestor_1(head, node1, node2)
    print ancestor.val
