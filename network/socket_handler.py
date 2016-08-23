import SocketServer
import socket


class EchoHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        print "Got connection from : " , self.client_address
        data = "sandeep"
        while len(data):
            data = self.request.recv(1024)
            print "Client Send: " + data
            self.request.send(data)
        print "Client left"


serverAddr = ("0.0.0.0", 9000)
server = SocketServer.TCPServer(serverAddr, EchoHandler)
server.serve_forever()

#Is this server multi-threaded?
#Code up the multi-threaded version of the Socket server
