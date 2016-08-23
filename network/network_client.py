import socket
import sys

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(("127.0.0.1", 7000))
while 1:
    user_input = raw_input("Please enter message to send to server")
    tcp_socket.send(user_input)
    print tcp_socket.recv(2048)

