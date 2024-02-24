# Networking With Scapy 👋


## Project Description
Welcome to Networking With Scapy, a Python project focused on studying and implementing various networking layers using Scapy. This project aims to provide a hands-on learning experience in networking protocols and packet manipulation techniques.

### Motive
The primary goal of this project is to deepen understanding and practical skills in networking by exploring different layers of the OSI model and implementing them using Scapy. By leveraging Scapy's capabilities, we can craft, send, receive, and analyze packets at different network layers, enabling us to grasp fundamental concepts more effectively.

#### Instructions
1. Ensure you have Scapy installed. If not, you can install it via pip:

    ```
    pip install scapy
    ```

## Day 4

## Transmission Control Protocol (TCP)
TCP, an essential component of the Internet Protocol Suite, provides reliable, ordered, and error-checked delivery of data between applications running on hosts communicating via an IP network. It operates at the transport layer of the OSI model, facilitating communication between devices over a network.

# Key Features:

Reliability: TCP ensures that data is reliably delivered to the intended recipient by establishing a connection-oriented communication between sender and receiver. It guarantees that data is received in the correct order without errors, retransmitting any lost packets.\

Connection Establishment and Termination: TCP employs a three-way handshake mechanism for connection establishment, where both sender and receiver exchange synchronization (SYN) and acknowledgment (ACK) packets. Similarly, it gracefully terminates connections using a four-way handshake.\

Flow Control: TCP employs flow control mechanisms to prevent overwhelming the receiver with data. It uses sliding window techniques, dynamically adjusting the amount of data sent based on the receiver's buffer capacity.\

Congestion Control: TCP incorporates congestion control algorithms to manage network congestion, ensuring fair and efficient data transmission. It adjusts the transmission rate based on network conditions, avoiding network congestion and packet loss.\

Full-Duplex Communication: TCP supports full-duplex communication, allowing data to be transmitted simultaneously in both directions. This enables bi-directional communication between client and server applications.\

## Usage:
TCP is extensively used in various applications such as web browsing, email, file transfer, and remote administration.\

It serves as the foundation for numerous protocols and services, including HTTP, FTP, SSH, and Telnet, facilitating reliable communication over the internet.
## Implementation:

TCP functionality is typically implemented in software libraries, networking stacks, and operating systems, providing developers with APIs for creating networked applications.\

Various programming languages offer TCP socket APIs for establishing TCP connections, sending and receiving data, and managing network communication.
TCP's robustness, reliability, and versatility make it one of the most widely used protocols for transmitting data over networks, playing a vital role in modern internet communication.



# Sending TCP and UDP packets using Scapy over IPv4
```
from scapy.all import IP, TCP, UDP, send

# Create an IPv4 packet with TCP protocol
ipv4_tcp_packet = IP(src="192.168.1.2", dst="8.8.8.8") / TCP(dport=80)

# Create an IPv4 packet with UDP protocol
ipv4_udp_packet = IP(src="192.168.1.2", dst="8.8.8.8") / UDP(dport=53)

# Send the TCP packet
send(ipv4_tcp_packet)

# Send the UDP packet
send(ipv4_udp_packet)

```

![image](https://github.com/karkibibak9/NetworkingWithPython/assets/47566089/d1d63450-3462-4603-b1e8-6df5443c6189)


## 🤝 Contributing

Contributions, issues and feature requests are welcome!


## Show your support

Give a ⭐️ if this project helped you!
