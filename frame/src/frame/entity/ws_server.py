# -*- coding:utf-8 -*-
"""
"""
__date__ = "31/07/2017"
__author__ = "zhaojm"

from frame.core.ws_entity import WSServerEntity


class WSServer(WSServerEntity):
    def __init__(self):
        pass

    def on_connect(self, request):
        pass

    def on_open(self):
        pass

    def on_message(self, payload, isBinary):
        pass

    def on_close(self, wasClean, code, reason):
        pass
