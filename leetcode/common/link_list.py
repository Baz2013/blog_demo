# -*- coding:utf-8 -*-

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


if __name__ == '__main__':
    head = creat_link([1, 2, 3, 4, 5, 6])
    travel_link(head)
