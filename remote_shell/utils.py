# -*- coding:utf-8 -*-

"""
utilitis function or method
"""

import os
import sys
import re


def read_config(r_config_file):
    """
    :param r_config_file: 配置文件
    :return:
    """
    if not os.path.exists(r_config_file):
        print "config file %s not exists" % (r_config_file,)
        sys.exit(1)
    with open(r_config_file) as handle:
        lines = handle.readlines()

    ret_rst = {}
    key = ''
    for line in lines:
        line = line.strip('\n\r')
        if not line:
            continue
        if line.startswith('['):
            key = line[1:-1]
        else:
            lst = ret_rst.get(key, [])
            lst.append(line)
            ret_rst[key] = lst

    return ret_rst


def print_output(r_lst):
    """
    打印命令行输出的内容
    :param r_lst:
    :return:
    """
    for line in r_lst:
        print line


def get_hosts(r_config, r_dest):
    """
    :param r_config: 主机组配置[dir]
    :param r_dest: 目标主机组 [str]
    :return: [list]
    """
    matched_str = []
    rst = []

    for key in r_config.keys():
        if re.match(r_dest, key):
            matched_str.append(key)

    for key in matched_str:
        rst += r_config.get(key)

    # print rst
    return rst


def red_font(s):
    """
    显示红字
    :param s:
    :return:
    """
    return "%s[31;2m%s%s[0m" % (chr(27), s, chr(27))


def green_font(s):
    """
    显示绿字
    :param s:
    :return:
    """
    return "%s[32;2m%s%s[0m" % (chr(27), s, chr(27))


def split_copy_command(r_str):
    """
    'src = /abc/123/a.txt dest=/def/user/' => ['/abc/123/a.txt', '/def/user/']
    :param r_str: [str]
    :return: [list]
    """
    t_lst = re.split('=| ', r_str)
    lst = []
    for s in t_lst:
        if s not in ['src','','dest']:
            lst.append(s)

    return lst



if __name__ == '__main__':
    print read_config('./rcm.conf')
