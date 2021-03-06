# -*- coding:utf-8 -*-
"""
Created on 10/06/2017

@author: zhaojm
"""

from twisted.internet import protocol, reactor


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print '......'
        print data
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


echo = EchoFactory()
reactor.listenTCP(8888, echo)
reactor.run()
