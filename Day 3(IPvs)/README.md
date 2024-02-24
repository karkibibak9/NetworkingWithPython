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
 0                   1                   2                   3   
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |       Header Checksum         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                         Source Address                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                      Destination Address                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (if any)                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                   Padding (if necessary)                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Version (4 bits): Indicates the version of IP being used. For IPv4, this field is set to 4.
IHL (Internet Header Length) (4 bits): Specifies the length of the header in 32-bit words.
Type of Service (8 bits): Originally intended for Quality of Service (QoS) parameters.
Total Length (16 bits): Length of entire IP packet (header + data).
Identification (16 bits): Unique value assigned to each packet for reassembly.
Flags (3 bits) and Fragment Offset (13 bits): Used for fragmentation and reassembly of packets.
Time to Live (8 bits): Prevents packets from circulating endlessly in the network.
Protocol (8 bits): Specifies the protocol used in the data portion of the packet (e.g., TCP, UDP).
Header Checksum (16 bits): Error-checking for the header.
Source Address (32 bits) and Destination Address (32 bits): IPv4 addresses of the sender and recipient.
Options (if any) (variable length): May include options such as timestamps or security information.
Padding (if necessary): Added to ensure that the header is a multiple of 32 bits.

## IPv6 (Internet Protocol version 6):

IPv6 is the latest version of the Internet Protocol, designed to succeed IPv4.
It uses a 128-bit address scheme, providing an exponentially larger pool of available addresses compared to IPv4.
IPv6 addresses are written in hexadecimal notation, consisting of eight groups of four hexadecimal digits separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).
In addition to addressing the issue of address exhaustion, IPv6 offers other improvements such as simplified header format, better support for quality of service (QoS), and built-in security features.
In summary, while IPv4 has been the backbone of the internet for many years, IPv6 represents the future of internet addressing, providing a vast pool of addresses to accommodate the ever-growing number of connected devices and ensuring the continued expansion and functionality of the internet. However, the transition from IPv4 to IPv6 has been gradual due to the need for compatibility and the complexity of upgrading existing infrastructure and systems.

## IPv6 Header Format:
 0                   1                   2                   3   
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version| Traffic Class |           Flow Label                  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Payload Length        |  Next Header  |   Hop Limit    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                         Source Address                        +
|                                                               |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                      Destination Address                      +
|                                                               |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Version (4 bits): Indicates the version of IP being used. For IPv6, this field is set to 6.
Traffic Class (8 bits) and Flow Label (20 bits): Traffic class allows for packet prioritization, while flow label facilitates flow identification.
Payload Length (16 bits): Length of the payload (data) portion of the packet.
Next Header (8 bits): Specifies the type of the next header after the IPv6 header (e.g., TCP, UDP).
Hop Limit (8 bits): Similar to Time to Live in IPv4, limits the number of hops a packet can traverse.
Source Address (128 bits) and Destination Address (128 bits): IPv6 addresses of the sender and recipient.


# Sending Payload using Scapy over Ethernet



## 🤝 Contributing

Contributions, issues and feature requests are welcome!


## Show your support

Give a ⭐️ if this project helped you!
