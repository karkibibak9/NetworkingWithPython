# Networking With Scapy 👋


## Project Description
Welcome to Networking With Scapy, a Python project focused on studying and implementing various networking layers using Scapy. This project aims to provide a hands-on learning experience in networking protocols and packet manipulation techniques.

### Motive
The primary goal of this project is to deepen understanding and practical skills in networking by exploring different layers of the OSI model and implementing them using Scapy. By leveraging Scapy's capabilities, we can craft, send, receive, and analyze packets at different network layers, enabling us to grasp fundamental concepts more effectively.

## Day 2
### Sending Ethernet Frames using Scapy
This Python script demonstrates how to use Scapy to craft and send Ethernet frames.

#### Instructions
1. Ensure you have Scapy installed. If not, you can install it via pip:

    ```
    pip install scapy
    ```

# Sending Payload using Scapy over Ethernet

This Python script demonstrates how to use Scapy to craft and send Ethernet frames with a custom payload.

## Code Explanation

```python
from scapy.all import Ether, sendp, Raw

# Asking user for payload
user_input = input("Enter Payload: ")

# Encoding the string to bytes
payload_data = user_input.encode()

# Crafting Ethernet Frame with Payload
ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff", src="11:22:33:44:55:66") / Raw(load=payload_data)

# Print Ethernet Frame Summary
print("Ethernet Frame Summary:")
print(ether_frame.summary())

# Sending the Ethernet Frame
sendp(ether_frame, iface="eth0")
```

# Sending Payload using Scapy over Ethernet

## Introduction
This Python script demonstrates how to use Scapy to send payloads over Ethernet frames. The script utilizes Scapy's packet crafting capabilities to construct Ethernet frames with custom payloads and sends them over the network interface specified.

## Code Explanation
```python
# Importing Scapy
from scapy.all import sniff, Ether, Raw

# Define a callback function to handle incoming packets
def packet_handler(packet):
    if packet.haslayer(Ether) and packet.haslayer(Raw):
        # Extract the source and destination MAC addresses
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
        # Extract the payload from Ethernet Frame
        payload = packet[Raw].load
        
        # Attempt to decode the payload
        try:
            decoded_payload = payload.decode('utf-8')
            print(f"Destination MAC Address: {dst_mac}")
            print("Received Ethernet Frame Payload:")
            print(decoded_payload)
        except UnicodeDecodeError:
            print("Received Ethernet Frame with Non-UTF-8 Payload:")
            print("Error Source MAC Address:", src_mac)

# Start sniffing for Ethernet frames on the specified interface
print("Sniffing for Ethernet Frames...")
sniff(prn=packet_handler, count=25, iface="eth0")
```
## 🤝 Contributing

Contributions, issues and feature requests are welcome!


## Show your support

Give a ⭐️ if this project helped you!
