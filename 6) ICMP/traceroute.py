import sys
from scapy.all import ICMP, IP, sr1

def traceroute(destination, gateway):
    # Send ICMP Echo Request packets with varying TTL values
    for ttl in range(1, 30):
        icmp_pkt = IP(dst=destination, ttl=ttl) / ICMP()
        response = sr1(icmp_pkt, timeout=2, verbose=False)
        
        # Check if response received
        if response:
            print(f"{ttl}: {response.src}")
            if response.src == destination or response.src == gateway:
                break
        else:
            print(f"{ttl}: *")


if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python traceroute.py <destination_ip> <gateway_ip>")
        sys.exit(1)

    destination_ip = sys.argv[1]
    gateway_ip = sys.argv[2]

    # Traceroute
    traceroute(destination_ip, gateway_ip)
