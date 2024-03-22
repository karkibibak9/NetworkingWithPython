# Networking with Python

This repository contains Python scripts for practicing different network protocols using Scapy.

## Network Layers:

1. **Physical Layer (Layer 1):** 
    - [IEEE 802.3](https://github.com/karkibibak9/NetworkingWithPython/tree/main/1%29%20IEEE%20802.3): This protocol operates at the physical layer of the OSI model and defines the standards for Ethernet networks.
    <details>
    <summary><b>Script: Receiving_and_Analyzing_Ethernet_Frames.py</b></summary>

    Sniffing Ethernet frames, extracting MAC addresses.

    </details>

    <details>
    <summary><b>Script: Sending_an_Ethernet_Frame_using_scapy.py</b></summary>

    Creating and sending Ethernet frame.

    </details>

    - [Ethernet payload using Scapy](https://github.com/karkibibak9/NetworkingWithPython/tree/main/2%29%20Ethernet%20payload%20using%20Scapy): This script focuses on creating Ethernet frames and customizing their payloads using Scapy.
    <details>
    <summary><b>Script: Crafted_payload_Reading_over_Ethernet_Frame.py</b></summary>

    Sniffing Ethernet frames, extracting MAC addresses.

    </details>

    <details>
    <summary><b>Script: Crafting_playload_in_Ethernet.py</b></summary>

    Creating and sending Ethernet frame.

    </details>

2. **Network Layer (Layer 3):** 
    - [IPvs](https://github.com/karkibibak9/NetworkingWithPython/tree/main/3%29%20IPvs): This protocol operates at the network layer and includes both IPv4 and IPv6 protocols.
    <details>
    <summary><b>Script: iprequest.py</b></summary>

    Sending TCP and UDP packets using Scapy over IPv4.

    </details>

3. **Transport Layer (Layer 4):** 
    - [TCP](https://github.com/karkibibak9/NetworkingWithPython/tree/main/4%29%20TCP): Transmission Control Protocol (TCP) is a connection-oriented protocol that operates at the transport layer. The script demonstrates TCP packet creation and manipulation using Scapy.
    <details>
    <summary><b>Script: TCPpackets.py</b></summary>

    Sending TCP packets using Scapy over IPv4.

    </details>

    - [UDP](https://github.com/karkibibak9/NetworkingWithPython/tree/main/5%29%20UDP): User Datagram Protocol (UDP) is a connectionless protocol that operates at the transport layer. The script showcases UDP packet creation and manipulation using Scapy.
    <details>
    <summary><b>Script: UDPpacket.py</b></summary>

    Sending UDP packets using Scapy over IPv4.

    </details>

4. **Internet Layer (Layer 3):**
    - [ICMP](https://github.com/karkibibak9/NetworkingWithPython/tree/main/6%29%20ICMP): Internet Control Message Protocol (ICMP) is used for diagnostic and control purposes within IP networks. The script focuses on ICMP packet creation and manipulation using Scapy.
