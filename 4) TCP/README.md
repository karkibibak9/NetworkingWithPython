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


## Transmission Control Protocol (TCP)
TCP, an essential component of the Internet Protocol Suite, provides reliable, ordered, and error-checked delivery of data between applications running on hosts communicating via an IP network. It operates at the transport layer of the OSI model, facilitating communication between devices over a network.

# Key Features:

Reliability: TCP ensures that data is reliably delivered to the intended recipient by establishing a connection-oriented communication between sender and receiver. It guarantees that data is received in the correct order without errors, retransmitting any lost packets.

Connection Establishment and Termination: TCP employs a three-way handshake mechanism for connection establishment, where both sender and receiver exchange synchronization (SYN) and acknowledgment (ACK) packets. Similarly, it gracefully terminates connections using a four-way handshake.

Flow Control: TCP employs flow control mechanisms to prevent overwhelming the receiver with data. It uses sliding window techniques, dynamically adjusting the amount of data sent based on the receiver's buffer capacity.

Congestion Control: TCP incorporates congestion control algorithms to manage network congestion, ensuring fair and efficient data transmission. It adjusts the transmission rate based on network conditions, avoiding network congestion and packet loss.

Full-Duplex Communication: TCP supports full-duplex communication, allowing data to be transmitted simultaneously in both directions. This enables bi-directional communication between client and server applications.

## Usage:

TCP is extensively used in various applications such as web browsing, email, file transfer, and remote administration.

It serves as the foundation for numerous protocols and services, including HTTP, FTP, SSH, and Telnet, facilitating reliable communication over the internet.

## Implementation:

TCP functionality is typically implemented in software libraries, networking stacks, and operating systems, providing developers with APIs for creating networked applications.

Various programming languages offer TCP socket APIs for establishing TCP connections, sending and receiving data, and managing network communication.
TCP's robustness, reliability, and versatility make it one of the most widely used protocols for transmitting data over networks, playing a vital role in modern internet communication.



# Sending TCP packets using Scapy over IPv4
```
from scapy.all import *
ip = IP(src="192.168.1.2", dst="192.168.1.1")
tcp = TCP(sport=6555, dport=80, flags="S", seq=1080)
packet = ip/tcp

send(packet)
```
## Wireshark Summery
36	27.147600464	192.168.1.2	192.168.1.1	TCP	54	6555 → 80 [SYN] Seq=0 Win=8192 Len=0


## 🤝 Contributing

Contributions, issues and feature requests are welcome!


## Show your support

Give a ⭐️ if this project helped you!
