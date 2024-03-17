import sys
from scapy.all import IP, ICMP, send



def icmp_redirect(destination, gateway):
    # Craft ICMP Redirect packet
    icmp_pkt = IP(dst=destination, gw=gateway) / ICMP(type=5, code=1)

    # Send packet
    send(icmp_pkt, verbose=False)

if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Usage: sudo python ICMP_Redirect.py <Dst ip> <Gateway ip>")
        sys.exit(1)
    destination_ip = sys.argv[1]
    gateway_ip = sys.argv[2]

    # ICMP Redirect
    icmp_redirect(destination_ip, gateway_ip)
