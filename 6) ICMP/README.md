# Networking With Scapy 👋

## Project Description
Welcome to Networking With Scapy, a Python project focused on studying and implementing various networking layers using Scapy. This project aims to provide a hands-on learning experience in networking protocols and packet manipulation techniques.

### Motive
The primary goal of this project is to deepen understanding and practical skills in networking by exploring different layers of the OSI model and implementing them using Scapy. By leveraging Scapy's capabilities, we can craft, send, receive, and analyze packets at different network layers, enabling us to grasp fundamental concepts more effectively.

#### Instructions
1. Ensure you have Scapy installed. If not, you can install it via pip:

    ```bash
    pip install scapy
    ```

## Internet Control Message Protocol (ICMP)

ICMP, a crucial protocol within the Internet Protocol Suite, facilitates communication between network devices to convey error messages and control information. It operates at the network layer of the OSI model, providing feedback about packet delivery and network status.

### Key Features:

1. **Error Reporting**: ICMP is primarily used for reporting errors encountered during packet processing or network operation. It enables routers and hosts to communicate error conditions to other devices.

2. **Diagnostic Tools**: ICMP supports diagnostic tools such as ping and traceroute, which help in testing connectivity, measuring round-trip times, and identifying network issues.

3. **Echo Requests and Replies**: ICMP allows hosts to send echo request messages to another host, which responds with an echo reply message. This functionality is utilized by the ping utility for testing network reachability.

4. **Network Management**: ICMP includes messages for network management tasks, such as redirecting traffic, informing about unreachable destinations, and managing multicast groups.

### Usage:

ICMP is commonly used for troubleshooting network connectivity issues, diagnosing network problems, and managing network traffic. It provides essential feedback mechanisms for ensuring efficient packet delivery and network operation.

### Implementation:

ICMP functionality is integrated into networking stacks and operating systems, providing support for generating and processing ICMP messages. Developers can utilize ICMP APIs for implementing network diagnostic tools and error handling mechanisms.

Programming languages offer libraries and modules for interacting with ICMP packets, enabling developers to create custom network management applications and diagnostic utilities.

ICMP's role in providing error reporting and network diagnostics contributes to efficient network troubleshooting and management, enhancing the reliability and performance of networked systems.

## Sending ICMP packets using Scapy over IPv4
```python
from scapy.all import IP, ICMP, send

# Create an IPv4 packet with ICMP protocol (Echo Request)
ipv4_icmp_packet = IP(src="192.168.1.2", dst="8.8.8.8") / ICMP(type=8, code=0)  # Type 8 for Echo Request, Code 0 for default

# Send the ICMP packet
send(ipv4_icmp_packet)


## 🤝 Contributing

Contributions, issues and feature requests are welcome!


## Show your support

Give a ⭐️ if this project helped you!
