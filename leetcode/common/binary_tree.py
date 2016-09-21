# -*- coding:utf-8 -*-
global LIST_POINT
LIST_POINT = 0


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creat_binary_tree(r_data_lst):
    """
    根据数据列表创建二叉树
    :param r_data_lst:
    :return: 头结点
    """
    global LIST_POINT
    tmp = r_data_lst[LIST_POINT]
    LIST_POINT += 1
    # print '--->{0}'.format(tmp)
    if '*' == tmp:
        head = None
    else:
        head = TreeNode(tmp)
        head.left = creat_binary_tree(r_data_lst)
        head.right = creat_binary_tree(r_data_lst)

    return head


def pre_order_travel(r_head):
    """
    :param head:
    :return:
    """
    if r_head is None:
        return
    print r_head.val,
    pre_order_travel(r_head.left)
    pre_order_travel(r_head.right)

def mid_order_travel(r_head):
    """
    :param head:
    :return:
    """
    if r_head is None:
        return
    mid_order_travel(r_head.left)
    print r_head.val,
    mid_order_travel(r_head.right)

def after_order_travel(r_head):
    """
    :param head:
    :return:
    """
    if r_head is None:
        return
    after_order_travel(r_head.left)
    after_order_travel(r_head.right)
    print r_head.val,


def modifyConstant():
    global LIST_POINT
    print LIST_POINT
    LIST_POINT += 1
    return


if __name__ == '__main__':
    data = [6, 2, 0, '*', '*', 4, 3, '*', '*', 5, '*', '*', 8, 7, '*', '*', 9, '*', '*']
    head = creat_binary_tree(data)
    # print head.left.right.right.val
    pre_order_travel(head)
    print
    mid_order_travel(head)
    print
    after_order_travel(head)
    # modifyConstant()
    # modifyConstant()
    # modifyConstant()
