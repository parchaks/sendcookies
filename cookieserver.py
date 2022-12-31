#!/bin/python

from http import server 
from http.cookies import SimpleCookie
import socketserver

port = 1234

class MyHTTPRequestHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        cookies = SimpleCookie(self.headers.get('Cookie'))
        with open('server.log','a') as f:
            f.write(f"\n {self.headers['Host']} : {cookies} \n")
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(('',port), MyHTTPRequestHandler) as httpd:
        print(f'Starting server at port {port}, use <Ctrl-C> to stop')
        httpd.serve_forever()
