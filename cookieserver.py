#!/bin/python

from http import server 
import socketserver

port = 1234
log_file= 'server.log'
class MyHTTPRequestHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        host = self.headers['Host']
        cookies = self.headers['session']
        with open(log_file,'a') as f:
            f.write(f"\n {host}:{cookies} \n")
        self.send_response(200)
        self.end_headers()

if __name__ == '__main__':
    with socketserver.TCPServer(('',port), MyHTTPRequestHandler) as httpd:
        print(f'Starting server at port {port}, use <Ctrl-C> to stop')
        httpd.serve_forever()
