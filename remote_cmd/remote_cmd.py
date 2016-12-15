#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import time
import ConfigParser

if os.name != 'nt':
    sys.path.append('/cbss/app/user/gucb/pexpect')
else:
    pass
import pexpect
import pxssh


def auto_ssh(r_user, r_passwd, r_host, r_cmd_list):
    """
    :param r_user:
    :param r_passwd:
    :param r_host:
    :param r_cmd_list:
    :return:
    """
    result = list()

    print 'cmd_lst:',
    print r_cmd_list

    try:
        ssh = pxssh.pxssh()
        ssh.login(r_host, r_user, r_passwd, login_timeout=1)
        for cmd in r_cmd_list:
            ssh.sendline(cmd)
            ssh.prompt()
            # print ssh.before
            result.append(ssh.before)
        ssh.logout()
    except pxssh.ExceptionPxssh, e:
        print 'pxssh failed to login' + ':' + r_host
        print 'exception info: %s' % (str(e),)
        # print str(e)
    return result


def scp_file(r_user, r_ip, r_remote_path, r_file, r_passwd):
    """
    将当前主机的文件拷贝到远程主机的目录下
    :param r_user: 远程主机用户名
    :param r_ip: 远程主机ip
    :param r_remote_path: 远程主机路径
    :param r_file: 当期主机文件
    :param r_passwd: 远程主机密码
    :return:
    """
    print 'scp %s %s@%s:%s' % (r_file, r_user, r_ip, r_remote_path)
    child = pexpect.spawn('scp %s %s@%s:%s' % (r_file, r_user, r_ip, r_remote_path))
    try:
        child.expect('password: ', timeout=2)
    except pexpect.TIMEOUT:
        print 'time out'
        return False
    child.sendline('%s' % r_passwd)
    time.sleep(.2)
    print 'success'
    return True


def read_conf(r_conf_file):
    """
    :param r_conf_file: 配置文件
    :return: 主机列表，列表元素为配置元组(ip,user,passwd)
    """
    res_lst = list()
    cfg = ConfigParser.ConfigParser()
    cfg.read(r_conf_file)
    sections = cfg.sections()
    for section in sections:
        host_user = cfg.get(section, 'host_user')
        host_ip = cfg.get(section, 'host_ip')
        host_passwd = cfg.get(section, 'host_passwd')
        res_lst.append((host_ip, host_user, host_passwd))

    return res_lst


def exec_cmd(r_conf_list, r_cmd_str):
    """
    执行命令
    :param r_conf_list: 主机配置列表, (ip,user,passwd)
    :param r_cmd_str: 输入的命令
    :return: 执行结果
    """
    if 'scp' in r_cmd_str:
        items = r_cmd_str.split(' ')
        for host_info in r_conf_list:
            print 'host_info:%s' % (host_info,)
            scp_file(host_info[1], host_info[0], items[2], items[1], host_info[2])
        return 'success'
    else:
        for host_info in r_conf_list:
            res = auto_ssh(host_info[1], host_info[2], host_info[0], [r_cmd_str])
            print res
        return


def main(r_conf_file):
    """
    入口函数
    :param r_conf_file: 配置文件
    :return:
    """
    conf_list = read_conf(r_conf_file)
    print conf_list
    while True:
        input_str = raw_input('>>')
        # print ':' + input_str
        if input_str == 'quit' or input_str == 'exit' or input_str == 'bye':
            sys.exit(0)
        elif input_str == '\n':
            continue

        exec_res = exec_cmd(conf_list, input_str)
        print exec_res
        time.sleep(0.1)


if __name__ == '__main__':
    if os.name == 'nt':
        main('E:\\dev_project\\rcm.conf')
    else:
        main('./rcm.conf')
