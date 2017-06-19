# -*- coding:utf-8 -*-
'''
Created on 19/06/2017

@author: zhaojm
'''


class CmdHandler(object):
    def __init__(self, client):
        self.client = client
        self.conn = None
        pass

    def __conn_to_server(self, ip, port):
        self.client.conn_to_server(ip, port)
        pass

    def on_made(self, conn):
        self.conn = conn
        pass

    def on_lost(self, conn):
        pass

    def on_msg(self, conn, msg):
        # 这里解析命令
        # 并分发命令
        if "conn" in msg:
            self.__conn_to_server(msg['ip'], msg['port'])

        pass

    def on_chan(self, chan, msg):
        pass
