# -*- coding:utf-8 -*-

# 141. Linked List Cycle  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?
#
# Subscribe to see which companies asked this question

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common.link_list import *


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        flag = True
        slow = head
        fast = head.next

        while slow != fast:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                flag = False
                break

        return flag


if __name__ == '__main__':
    root = create_link_with_cycle([1, 2, 3, 4, 5, 6, 7])
    s = Solution()
    print s.hasCycle(root)
    root = create_link([1])
    print s.hasCycle(root)

    root = create_link([1, 2, 3])
    print s.hasCycle(root)
