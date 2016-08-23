import socket
import struct


raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
raw_socket.bind(("wlan0", socket.htons(0x0800)))
packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')
raw_socket.send(packet + "Hello there")


"""
Exercise: Inject an ARP Request packet with the raw socket and verified it by wireshark or tcpdump
"""