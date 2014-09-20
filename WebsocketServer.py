#!/usr/bin/env python

# import asyncio
# import websockets
import CopyPasta

from ws4py.websocket import WebSocket
from gevent import monkey; monkey.patch_all()
from ws4py.websocket import EchoWebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication

class CopyPastaSocket(WebSocket):
    def received_message(self, message):
        self.send(CopyPasta.generate_copy_pasta(message.data), message.is_binary)
        print(message.data)
        self.send(CopyPasta.generate_copy_pasta(message.data), message.is_binary)

server = WSGIServer(('localhost', 3001), WebSocketWSGIApplication(handler_cls=CopyPastaSocket))
server.serve_forever()

# @asyncio.coroutine
# def hello(websocket, path):
#     message = yield from websocket.recv()
#     print("Received message {}".format(message))
#     result = CopyPasta.generate_copy_pasta(message)
#     yield from websocket.send(result)
#     print("Sent message: {}".format(result))

# start_server = websockets.serve(hello, 'localhost', 3001)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
