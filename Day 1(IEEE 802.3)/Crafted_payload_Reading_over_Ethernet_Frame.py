# from scapy.all import sniff, Ether

# #callback Function
# def packet_handler(packet):
#     if packet.haslayer(Ether) and packet.payload:
#         #Extracting the payload from Eyhernet Frame
#         payload = packet.payload
#         if isinstance(payload, bytes):
#             decoded_payload = payload.decode()
#             print('Received Ethernet Frame Payload')
#             print(decoded_payload)

# #starting to sniff
# print("Sniffing for Ethernet Frames")
# sniff(prn=packet_handler, count=10, iface="lo")

from scapy.all import sniff, Ether, Raw

# Define a callback function to handle incoming packets
def packet_handler(packet):
    if packet.haslayer(Ether) and packet.haslayer(Raw):
        # Extract the source and destination MAC addresses
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
        # print(src_mac, dst_mac)
        # Extract the payload from Ethernet Frame
        payload = packet[Raw].load
        
        # Check if the payload is in bytes and decode it
         #Attempt to decode the payload
        try:
            decoded_payload = payload.decode('utf-8')
            # hex shit!!!!
            # print("Received Ethernet Frame:")
            # print(f"Source MAC Address: {src_mac}")
            print(f"Destination MAC Address: {dst_mac}")
            print("Received Ethernet Frame Payload:")
            print(decoded_payload)
        except UnicodeDecodeError:
            print("Received Ethernet Frame with Non-UTF-8 Payload:")
            print("error Source MAC Address:", src_mac)
            # print("Destination MAC Address:", dst_mac)
            # print("Payload (hex):", payload.hex())

# Start sniffing for Ethernet frames on the loopback interface
print("Sniffing for Ethernet Frames...")
sniff(prn=packet_handler, count=25, iface="eth0")
