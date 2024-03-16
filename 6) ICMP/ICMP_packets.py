from scapy.all import IP, ICMP, send

# Create an IPv4 packet with ICMP protocol (Echo Request)
ipv4_icmp_packet = IP(src="192.168.1.2", dst="8.8.8.8") / ICMP(type=8, code=0)  # Type 8 for Echo Request, Code 0 for default

# Send the ICMP packet
send(ipv4_icmp_packet)
