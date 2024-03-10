from scapy.all import IP, TCP, UDP, send

# Create an IPv4 packet with TCP protocol
ipv4_tcp_packet = IP(src="1.1.1.1", dst="8.8.8.8") / TCP(dport=80)

# Create an IPv4 packet with UDP protocol
ipv4_udp_packet = IP(src="1.1.1.1", dst="8.8.8.8") / UDP(dport=53)

# Send the TCP packet
send(ipv4_tcp_packet)

# Send the UDP packet
send(ipv4_udp_packet)
