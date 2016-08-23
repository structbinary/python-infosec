import SocketServer
import SimpleHTTPServer

"""
                           Creating a Simple HTTP Server
"""


class HTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/admin":
            self.wfile.write('This page is only for admins')
            self.wfile.write(self.headers)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)



serverAddr = ("0.0.0.0", 9000)
server = SocketServer.TCPServer(serverAddr, HTTPRequestHandler)
server.serve_forever()



"""
Exercise - Is there a module available to run CGI as well
           Please write a POC for the above
"""