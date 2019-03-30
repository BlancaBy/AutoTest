#coding=utf-8

import os, socket

# region 系统相关操作

# 执行cmd指令
def execute_cmd(cmd):
    p = os.popen(cmd)
    return p.read()

# 获取本地ip地址
def get_ip_address():
    hostname = get_hostname()
    ip = socket.gethostbyname(hostname)
    return ip

# 获取本机计算机名
def get_hostname():
    hostname = socket.gethostname()
    return hostname
# endregion