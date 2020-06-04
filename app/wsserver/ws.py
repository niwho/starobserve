# _*_coding:utf-8_*_
from autobahn.twisted.websocket import WebSocketServerProtocol
# from  autobahn.websocket.types import ConnectionRequest
from app import app
from http.cookies import SimpleCookie
from flask.sessions import SecureCookieSessionInterface
seFactory = SecureCookieSessionInterface()
'''

ss = seFactory.open_session()
ss.get(

)
'''


class MyServerProtocol(WebSocketServerProtocol):
    def __init__(self):
        super().__init__()
        self.cookies = {}

    def onConnect(self, request):
        from http.cookies import SimpleCookie
        s = SimpleCookie(request.headers["cookie"])
        val = s.get(app.session_cookie_name).value
        self.cookies = {
            app.session_cookie_name: val
        }
        ss = seFactory.open_session(app, self)

        print(ss.get("test"))
        print(request.params)
        return None

    def onConnecting(self, transport_details):
        print("onConnecting")
        return None

    def onOpen(self):
        print("onOpen")
        return None

    def onClose(self, wasClean, code, reason):
        print("onClose")
        return None

    def onMessage(self, payload, isBinary):
        ## echo back message verbatim
        self.sendMessage(payload, isBinary)
        # self.sendClose(code=None, reason=None)


if __name__ == '__main__':
    import sys

    from twisted.python import log
    from twisted.internet import reactor
    log.startLogging(sys.stdout)

    from autobahn.twisted.websocket import WebSocketServerFactory
    factory = WebSocketServerFactory()
    factory.protocol = MyServerProtocol

    reactor.listenTCP(9000, factory)
    reactor.run()
