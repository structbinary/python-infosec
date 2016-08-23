from scapy.all import *


#Subnet Scanner

for lsb in range(1,50):
    ip = "192.168.43." +str(lsb)
    arpRequest = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    arpResponse = srp1(arpRequest, timeout=1, verbose=0)
    if arpResponse:
        print "IP:" + arpResponse.psrc + "MAC: " + arpResponse.hwsrc




"""
Exercise1: Create a DNS poisoning tool similar to Dnsspoof using scapy
Exercise2: Create a ARP MITM tool using scapy
Exercise3: Create a TCP SYN Scanner using scapy
Exercise4: Explore how to create a fuzzer with scapy
Exercise5: Create a DNS Fuzzer with Scapy and try it against DNSspoof

"""