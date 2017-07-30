# -*- coding:utf-8 -*-
"""
Created on 26/06/2017

管理server, 用于管理

@author: zhaojm
"""
from frame.servers.rpc.rpc_server import RpcServer


class Server(RpcServer):

    def on_conn_lost(self, conn, reason):
        pass

    def on_conn_made(self, conn):
        pass

    def on_msg(self, conn, msg):
        conn.sendLine(msg)
        pass
