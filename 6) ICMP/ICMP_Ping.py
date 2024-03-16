import sys
from scapy.all import IP, sr1, ICMP
import time


def ping(destination):
    # Craft ICMP Echo Request packet
    icmp_pkt = IP(dst=destination) / ICMP()


    start_time = time.time()

    # Send packet and wait for response
    response = sr1(icmp_pkt, timeout=2, verbose=False)

    end_time = time.time()

    #RTT (Round_Trip Time)
    return_time = end_time-start_time

    # Check if response received
    if response:
        print(f"Response from {destination}: {response.summary()}, RTT: {return_time:.6f} seconds")
    else:
        print(f"No response from {destination}")

if __name__ == "__main__":
    #Checking the Argu
    if len(sys.argv) != 2:
        print("Usage: Python ICMP_Ping.py <Dst_IP>")
        sys.exit(1)

    destination_ip = sys.argv[1]
    ping(destination_ip)


