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

## Day 3 


## IPv4 (Internet Protocol version 4):

IPv4 is the fourth version of the Internet Protocol, and it has been the dominant protocol used on the internet for several decades.
It uses a 32-bit address scheme, allowing for approximately 4.3 billion unique addresses.
IPv4 addresses are typically written in dotted-decimal notation, consisting of four decimal numbers separated by periods (e.g., 192.168.0.1).
The rapid growth of the internet and the increasing number of connected devices have led to a depletion of available IPv4 addresses. This scarcity has necessitated the development of IPv6.

## IPv4 Header Format:


| Field                 | Size (bits) | Description                              |
|-----------------------|-------------|------------------------------------------|
| Version               | 4           | Version of IP (IPv4 = 4)                 |
| IHL (Header Length)  | 4           | Length of the header in 32-bit words     |
| Type of Service (TOS)| 8           | Quality of Service parameters            |
| Total Length          | 16          | Total length of the packet (header + data)|
| Identification        | 16          | Unique value for packet reassembly       |
| Flags                 | 3           | Flags for fragmentation control          |
| Fragment Offset       | 13          | Offset of the fragment in the original datagram |
| Time to Live (TTL)    | 8           | Limits packet lifetime in the network    |
| Protocol              | 8           | Protocol used in the data portion (e.g., TCP, UDP) |
| Header Checksum       | 16          | Error-checking for the header            |
| Source Address        | 32          | IPv4 address of the sender               |
| Destination Address   | 32          | IPv4 address of the recipient            |
| Options               | Variable    | Optional fields for various purposes     |
| Padding               | Variable    | Padding to ensure header is a multiple of 32 bits |



## IPv6 (Internet Protocol version 6):

IPv6 is the latest version of the Internet Protocol, designed to succeed IPv4.
It uses a 128-bit address scheme, providing an exponentially larger pool of available addresses compared to IPv4.
IPv6 addresses are written in hexadecimal notation, consisting of eight groups of four hexadecimal digits separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
In addition to addressing the issue of address exhaustion, IPv6 offers other improvements such as simplified header format, better support for quality of service (QoS), and built-in security features.
In summary, while IPv4 has been the backbone of the internet for many years, IPv6 represents the future of internet addressing, providing a vast pool of addresses to accommodate the ever-growing number of connected devices and ensuring the continued expansion and functionality of the internet. However, the transition from IPv4 to IPv6 has been gradual due to the need for compatibility and the complexity of upgrading existing infrastructure and systems.

## IPv6 Header Format

| Field                 | Size (bits) | Description                              |
|-----------------------|-------------|------------------------------------------|
| Version               | 4           | Version of IP (IPv6 = 6)                 |
| Traffic Class         | 8           | Traffic class for packet prioritization  |
| Flow Label            | 20          | Flow identification for specialized handling |
| Payload Length        | 16          | Length of the payload (data) portion     |
| Next Header           | 8           | Specifies the type of next header        |
| Hop Limit             | 8           | Limits the number of hops a packet can traverse |
| Source Address        | 128         | IPv6 address of the sender               |
| Destination Address   | 128         | IPv6 address of the recipient            |



# Sending Payload using Scapy over Ethernet

![image](https://github.com/karkibibak9/NetworkingWithPython/assets/47566089/d1d63450-3462-4603-b1e8-6df5443c6189)


## 🤝 Contributing

Contributions, issues and feature requests are welcome!


## Show your support

Give a ⭐️ if this project helped you!
