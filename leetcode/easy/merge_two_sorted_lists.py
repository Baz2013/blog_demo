# -*- coding:utf-8 -*-

# 21. Merge Two Sorted Lists  QuestionEditorial Solution  My Submissions
# Difficulty: Easy
# Merge two sorted linked lists and return it as a new list.
#  The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import common.link_list as ll


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        q = l2
        head = ll.ListNode(999)  # 提交到leetcode的时候 改为 head = ListNode(999)
        k = head
        while p is not None and q is not None:
            if p.val > q.val:
                k.next = q
                q = q.next
            else:
                k.next = p
                p = p.next
            k = k.next

        if q is not None:
            k.next = q
        elif p is not None:
            k.next = p
        else:
            pass
        return head.next


if __name__ == '__main__':
    head1 = ll.creat_link([1, 4, 7, 9])
    head2 = ll.creat_link((2, 3, 4, 6, 8, 9))
    s = Solution()
    new_head = s.mergeTwoLists(head1, head2)
    ll.travel_link(new_head)
