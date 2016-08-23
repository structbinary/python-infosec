import socket
import struct
import binascii

raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

pkt = raw_socket.recvfrom(2048)

ethernetHeader = pkt[0][0:14]
eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)
print "Client Hardware address is " + binascii.hexlify(eth_hdr[0])
print "Destination Hardware address is " + binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])

ipheader = pkt[0][14:34]
ip_hdr = struct.unpack('!12s4s4s', ipheader)
print "Source IP address is " + socket.inet_ntoa(ip_hdr[1])
print "Destination IP address is " + socket.inet_ntoa(ip_hdr[2])

tcpHeader = pkt[0][34:54]
tcp_hdr = struct.unpack("!HH16s", tcpHeader)
(source_port,dest_port,header) = tcp_hdr
print "Source port is %d" %dest_port
print "Destination port is %d" %source_port

"""
Exercise1 - Create a packet sniffer using raw sockets  which can parse TCP packets(parser individual field)
Exercise2 - Create a sniffer which uses a filter to only print details of an HTTP packet(TCP, Port 80)
            and also dump the data
"""



