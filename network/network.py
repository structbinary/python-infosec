import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket.bind(("0.0.0.0", 7000))
tcp_socket.listen(2)

print "Waiting for the client...."
(client, (ip, port)) = tcp_socket.accept()
print "Received connection from : ", ip
print "Starting ECHO output ..."
data = "sandeep"
while len(data):
    data = client.recv(2048)
    print "Client Sent : ", data
    client.send(data)

print "Closing connection ...."
client.close()
print "Shutting down server ...."
tcp_socket.close()

#create a simple echo server to handle 1 client
#create a multi threaded echo server
#create a multi process server
#create a non-blocking Multiplexed echo server using select()
