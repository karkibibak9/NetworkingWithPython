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