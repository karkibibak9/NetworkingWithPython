from scapy.all import IP, ICMP, sr1, send, RandShort

def ping(destination):
    # Craft ICMP Echo Request packet
    icmp_pkt = IP(dst=destination) / ICMP()

    # Send packet and wait for response
    response = sr1(icmp_pkt, timeout=2, verbose=False)

    # Check if response received
    if response:
        print(f"Response from {destination}: {response.summary()}")
    else:
        print(f"No response from {destination}")


def icmp_redirect(destination, gateway):
    # Craft ICMP Redirect packet
    icmp_pkt = IP(dst=destination, gw=gateway) / ICMP(type=5, code=1)

    # Send packet
    send(icmp_pkt, verbose=False)

# Example usage:
destination_ip = "192.168.1.1"
gateway_ip = "192.168.1.254"

# Ping
ping(destination_ip)


# ICMP Redirect
icmp_redirect(destination_ip, gateway_ip)
