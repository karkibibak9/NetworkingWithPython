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

## User Datagram Protocol (UDP)

UDP, another vital protocol within the Internet Protocol Suite, offers a connectionless and unreliable means of data transmission between applications running on hosts communicating via an IP network. It functions at the transport layer of the OSI model, enabling communication between devices over a network.

### Key Features:

1. **Connectionless Communication**: Unlike TCP, UDP does not establish a connection before sending data. It operates on a fire-and-forget basis, where packets are sent without prior setup.

2. **Unreliable Delivery**: UDP does not guarantee the delivery of data packets. It lacks mechanisms for acknowledgment, retransmission, and error correction, making it susceptible to packet loss.

3. **Low Overhead**: UDP has minimal overhead compared to TCP, as it does not maintain connection state information or perform error recovery. This makes it suitable for applications prioritizing low-latency communication.

4. **Simple Header Structure**: UDP packets consist of a lightweight header containing source and destination port numbers and a length field, contributing to faster packet processing and transmission.

5. **Broadcast and Multicast Support**: UDP supports broadcast and multicast communication, allowing packets to be sent to multiple recipients simultaneously.

### Usage:

UDP finds applications in scenarios where real-time data transmission and low-latency communication are critical, such as audio/video streaming, online gaming, DNS, and Voice over IP (VoIP).

It is preferred for applications where occasional packet loss or out-of-order delivery is acceptable, trading reliability for reduced latency.

### Implementation:

UDP functionality is implemented in software libraries, networking stacks, and operating systems, providing developers with APIs for creating networked applications.

Programming languages offer UDP socket APIs for establishing communication endpoints, sending and receiving datagrams, and handling UDP packet transmission.

UDP's lightweight nature and simplicity make it suitable for applications requiring fast and efficient data transmission, albeit at the cost of reliability compared to TCP.

## In UDP packets, specifying a source port is optional. If you don't specify a source port, the operating system's networking stack will automatically assign a source port for the outgoing UDP packet.

# Sending UDP packets using Scapy over IPv4
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
