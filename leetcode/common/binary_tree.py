# -*- coding:utf-8 -*-

import Queue

global LIST_POINT
LIST_POINT = 0


#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def creat_binary_tree(r_data_lst):
    """
    根据数据列表创建二叉树,列表为二叉树的先序序列,空节点用'*'表示,叶子节点后边跟两个'*'
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


def no_curv_pre_order_travel(r_head):
    """
    非递归遍先序历二叉树
    :param r_head:
    :return:
    """
    if r_head is None:
        return
    stack = list()  # 用list模拟栈
    res = list()
    stack.append(r_head)
    while len(stack) > 0:
        node = stack.pop()
        # print node.val
        res.append(node.val)
        if node.right and node.left:
            stack.append(node.right)
            stack.append(node.left)
        elif node.left:
            stack.append(node.left)
        elif node.right:
            stack.append(node.right)

    return res


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


def no_curv_mid_order_travel(r_head):
    """
    中序非递归遍历二叉树
    :param r_head:
    :return:
    """
    if r_head is None:
        return
    stack = list()
    res = list()


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


def level_order_traver(r_head):
    """
    二叉树层序遍历
    :param r_head:
    :return:
    """
    queue = Queue.Queue()
    queue.put(r_head)
    while queue.qsize() != 0:
        node = queue.get()
        print node.val,
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)


def modifyConstant():
    global LIST_POINT
    print LIST_POINT
    LIST_POINT += 1
    return


if __name__ == '__main__':
    data = [6, 2, 0, '*', '*', 4, 3, '*', '*', 5, '*', '*', 8, 7, '*', '*', 9, '*', '*']
    head = creat_binary_tree(data)
    # print head.left.right.right.val
    # pre_order_travel(head)
    # print
    # mid_order_travel(head)
    # print
    # after_order_travel(head)
    # print
    # level_order_traver(head)
    # # modifyConstant()
    # # modifyConstant()
    # # modifyConstant()
    print no_curv_pre_order_travel(head)
