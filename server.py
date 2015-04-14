#!/bin/python

import time
import SimpleHTTPServer
import SocketServer

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/simplehttpwebsite_content.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('127.0.0.1', 10011), Handler)

server.serve_forever()