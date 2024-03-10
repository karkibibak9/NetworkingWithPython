# Networking With Scapy 👋

### Project Description
Welcome to Networking With Scapy, a Python project focused on studying and implementing various networking layers using Scapy. This project aims to provide a hands-on learning experience in networking protocols and packet manipulation techniques.

### ✨ Motive
The primary goal of this project is to deepen understanding and practical skills in networking by exploring different layers of the OSI model and implementing them using Scapy. By leveraging Scapy's capabilities, we can craft, send, receive, and analyze packets at different network layers, enabling us to grasp fundamental concepts more effectively.


## IEEE 802.3
Ethernet is a set of technologies and protocols that are used primarily in LANs. It was first standardized in 1980s by IEEE 802.3 standard. IEEE 802.3 defines the physical layer and the medium access control (MAC) sub-layer of the data link layer for wired Ethernet networks.
Ethernet is classified into two categories: classic Ethernet and switched Ethernet.
![ieee_802_3](https://github.com/karkibibak9/NetworkingWithPython/assets/47566089/69ea9516-253f-4ce1-8ec4-031c38213b6c)
# Frame Format of Classic Ethernet and IEEE 802.3

The frame format of classic Ethernet and IEEE 802.3 consists of several key fields:

1. **Preamble:** 
   - In classic Ethernet, it's an 8-byte field providing timing pulses for transmission.
   - In IEEE 802.3, it's a 7-byte field serving the same purpose.

2. **Start of Frame Delimiter (SFD):** 
   - Found in IEEE 802.3 frames only, it's a 1-byte field with an alternating pattern of ones and zeros, ending with two ones.

3. **Destination Address:** 
   - A 6-byte field containing the physical address of the destination station.

4. **Source Address:** 
   - A 6-byte field containing the physical address of the sending station.

5. **Length:** 
   - A 2-byte field in classic Ethernet, storing the number of bytes in the data field.
   - Note: This field is replaced by the type/length field in IEEE 802.3, which may indicate either the length of the frame or the type of protocol being used.

6. **Data:** 
   - A variable-sized field carrying data from upper layers, with a maximum size of 1500 bytes.
   - Note: This field can vary depending on the payload being transmitted.

7. **Padding:** 
   - Additional bits added to the data to meet the minimum frame size requirement of 46 bytes in classic Ethernet.
   - Note: Padding ensures that the frame meets the minimum size requirement and helps maintain synchronization between sender and receiver.

8. **CRC (Cyclic Redundancy Check):** 
   - A field containing error detection information, ensuring data integrity during transmission.
   - Note: CRC is computed based on the contents of the frame and is used by the receiving station to detect transmission errors.

Overall, the frame format of classic Ethernet and IEEE 802.3 provides essential components for data transmission, including addressing, data payload, error detection, and synchronization mechanisms. The differences between classic Ethernet and IEEE 802.3 lie mainly in the preamble length and the presence of the start of frame delimiter. These standards ensure reliable communication over Ethernet networks.

## Sending Ethernet Frames using Scapy

This Python script demonstrates how to use Scapy to craft and send Ethernet frames.

## Instructions

1. Ensure you have Scapy installed. If not, you can install it via pip:
    ```bash
    pip install scapy
    ```

2. Copy the following Python code snippet into your Python script:

```
#importing Scapy
from scapy.all import Ether, sendp

#Creating Ethernet Frame
ether_Frame = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:55:88:55:44")

print("Ethernet_Frame Summery:")
print(ether_Frame.summary())

#sending the Frame
sendp(ether_Frame, iface="eth0")
```
# Sniffing Ethernet Frames with Scapy

This Python script demonstrates how to use Scapy to sniff Ethernet frames and extract header information.

## Instructions

1. Copy the following Python code snippet into your Python script:

```python
#importing Scapy
from scapy.all import sniff, Ether

#defining the callback function to handle incoming packets
def packet_caller(packet):
    if packet.haslayer(Ether):
        #Extracting the Header Information
        src_address = packet[Ether].src
        dst_address = packet[Ether].dst
        print(f"Source MAC Address {src_address}, Destination MAC address: {dst_address}")

#sniffing from Ethernet Frame
print("Sniffing for Ethernet Frames...")
sniff(prn=packet_caller, iface="eth0", count=10)
```
## 🤝 Contributing

Contributions, issues and feature requests are welcome!


## Show your support

Give a ⭐️ if this project helped you!
