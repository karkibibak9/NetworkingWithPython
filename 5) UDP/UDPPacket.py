from scapy.all import *

dst_ip = "192.168.1.1"
dst_port = 1223

src_ip = "192.168.1.2"
src_port = 80

udp_packet = UDP(dport=dst_port, sport=src_port) / Raw(load="Raw data is Sent")

send(IP(dst=dst_ip)/udp_packet)