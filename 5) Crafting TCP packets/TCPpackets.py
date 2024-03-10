from scapy.all import *
ip = IP(src="192.168.1.2", dst="192.168.1.1")
tcp = TCP(sport=6555, dport=80, flags="S", seq=1080)
packet = ip/tcp

send(packet)