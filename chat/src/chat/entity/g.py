# -*- coding:utf-8 -*-
"""
Created on 21/06/2017

本模块存储全局的一些数据, 方便随时随地引用

@author: zhaojm
"""

from frame.core import reactor
from frame.entity import log
import logging
from chat.entity import config_load

__cfg_path = "config/"

cfg = config_load.load(__cfg_path)


def init_servers_text():
    s_list_str = ["db", "gate", "manager", "robot", "proxy"]

    ip = "127.0.0.1"
    port = 8000

    for s_str in s_list_str:
        # register server
        # logging.debug("%s %s:%s" % (s_str, ip, port))
        s = "from chat.servers.%s import init_server; init_server('%s', %d);" % (s_str, ip, port)
        logging.info(s)
        exec s
        port += 1

    s_list_str = ['http', 'sdk']

    for s_str in s_list_str:
        # register web app
        # logging.debug("%s %s:%s" % (s_str, ip, port))
        s = "from chat.servers.%s import init_server; init_server('%s', %d, '%s');" % (s_str, ip, port, s_str)
        logging.info(s)
        exec s
        port += 1

    s_list_str = ['sio', 'ws']
    for s_str in s_list_str:
        # register web app
        url = u'ws://%s:%s' % (ip, port)
        # port += 1
        # logging.debug("%s %s:%s %s" % (s_str, ip, port, url))
        s = "from chat.servers.%s import init_server; init_server('%s', %d, '%s');" % (s_str, ip, port, url)
        logging.info(s)
        exec s
        port += 1


def init_servers():
    for server in cfg.get('servers'):
        s = "from chat.servers.%s import init_server; init_server(%s);" % (server['name'], server)
        logging.info(s)
        exec s


def setup_servers():
    log.init_logging()

    init_servers()
    reactor.start_reactor()
