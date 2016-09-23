# -*- coding:utf-8 -*-

# 24. Swap Nodes in Pairs
# Difficulty: Easy
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list,
# only nodes itself can be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import common.link_list as ll


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return

        pre = self
        pre.next = head

        while pre.next and pre.next.next:
            p = pre.next
            q = p.next
            pre.next, q.next, p.next = q, p, q.next
            pre = p

        # print new_head.val
        return self.next


if __name__ == '__main__':
    s = Solution()

    head = ll.creat_link([1, 2])
    ll.travel_link(head)
    head1 = s.swapPairs(head)
    ll.travel_link(head1)

    head = ll.creat_link([1, 2, 3])
    ll.travel_link(head)
    head1 = s.swapPairs(head)
    ll.travel_link(head1)

    head = ll.creat_link([1, 2, 3, 4])
    ll.travel_link(head)
    head1 = s.swapPairs(head)
    ll.travel_link(head1)
    #
    head = ll.creat_link([1, 2, 3, 4, 5, 6, 7])
    ll.travel_link(head)
    head1 = s.swapPairs(head)
    ll.travel_link(head1)
