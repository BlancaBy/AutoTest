# -*- coding:utf-8 -*-

import os,pymysql
from sshtunnel import SSHTunnelForwarder

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class MySql:
    def __init__(self, host, port, user, pwd, db, ssh_host, ssh_port, ssh_user, ssh_key):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.port = int(port)
        self.ssh_host = ssh_host
        self.ssh_port = int(ssh_port)
        self.ssh_user = ssh_user
        self.ssh_key = project_dir + ssh_key

    # def __GetConnect(self):
    #     with SSHTunnelForwarder(
    #             (self.ssh_host, self.ssh_port),  # 指定ssh登录的跳转机的address，端口号
    #             ssh_username = self.ssh_user,  # 跳转机的用户
    #             ssh_pkey = self.ssh_key,
    #             remote_bind_address = (self.host, self.port)) as server:  # mysql服务器的address，端口号
    #         self.conn = pymysql.connect(host = '127.0.0.1',  # 此处必须是是127.0.0.1
    #                                port = server.local_bind_port,
    #                                user = self.user, #数据库用户名
    #                                passwd = self.pwd, #数据库密码
    #                                db = self.db #数据库名称
    #                                )
    #         cur = self.conn.cursor()
    #         if not cur:
    #             raise(NameError, "连接数据库失败")
    #         else:
    #             return cur

    def ExecQuery(self, sql):
        with SSHTunnelForwarder(
                (self.ssh_host, self.ssh_port),  # 指定ssh登录的跳转机的address，端口号
                ssh_username = self.ssh_user,  # 跳转机的用户
                ssh_pkey = self.ssh_key,
                remote_bind_address = (self.host, self.port)) as server:  # mysql服务器的address，端口号
            conn = pymysql.connect(host = '127.0.0.1',  # 此处必须是127.0.0.1
                                   port = server.local_bind_port,
                                   user = self.user, #数据库用户名
                                   passwd = self.pwd, #数据库密码
                                   db = self.db #数据库名称
                                   )
            cur = conn.cursor()
            if not cur:
                raise(NameError, "连接数据库失败")
            else:
                cur.execute(sql)
                resList = cur.fetchall()
                #查询完毕后必须关闭连接
                conn.close()
                return resList

    def ExecNonQuery(self, sql):
        with SSHTunnelForwarder(
                (self.ssh_host, self.ssh_port),  # 指定ssh登录的跳转机的address，端口号
                ssh_username = self.ssh_user,  # 跳转机的用户
                ssh_pkey = self.ssh_key,
                remote_bind_address = (self.host, self.port)) as server:  # mysql服务器的address，端口号
            conn = pymysql.connect(host = '127.0.0.1',  # 此处必须是是127.0.0.1
                                   port = server.local_bind_port,
                                   user = self.user, #数据库用户名
                                   passwd = self.pwd, #数据库密码
                                   db = self.db #数据库名称
                                   )
            cur = conn.cursor()
            if not cur:
                raise(NameError, "连接数据库失败")
            else:
                cur.execute(sql)
                conn.commit()
                conn.close()