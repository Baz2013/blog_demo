# -*- coding:utf-8 -*-

# 83. Remove Duplicates from Sorted List
# Difficulty: Easy
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def travel_link(r_link):
    """
    :param r_link: list[List]
    :return:
    """
    p = r_link
    while p is not None:
        print p.val,
        p = p.next
    print


def creat_link(r_data_lst):
    """
    :param r_data_lst:
    :return:
    """
    if len(r_data_lst) == 0 or r_data_lst is None:
        return
    head = ListNode(r_data_lst[0])
    p = head
    for i in r_data_lst[1::]:
        p.next = ListNode(i)
        p = p.next

    return head


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        p = head
        q = head.next
        while q is not None:
            if p.val == q.val:
                p.next = q.next
                q = q.next
            else:
                if q is not None:
                    p = p.next
                    q = q.next
                else:
                    p = p.next

        return head


if __name__ == '__main__':
    head = creat_link([1, 1, 1, 3, 3])
    travel_link(head)

    s = Solution()
    head = s.deleteDuplicates(head)
    travel_link(head)

    head1 = creat_link([1, 1, 1])
    head1 = s.deleteDuplicates(head1)
    travel_link(head1)

    head1 = creat_link([])
    head1 = s.deleteDuplicates(head1)
    travel_link(head1)
