# from scapy.all import IP, sniff, DHCP, Ether, ls
# # ls()
# def DHCP_handler(packet):
#     if DHCP in packet:
#         print(DHCP)
#         if packet[DHCP].options[1][0] == 1:
#             print("DHCP Discover Packet Found")
#             print(packet.summary())

# def sniff_DHCP(interface: "eth0", count: 0):
#     print(f"Discovering the DHCP packet on {interface}")
#     sniff(iface="eth0", filter="udp and src port 68 and dst port 67" , prn=DHCP_handler, count=count)

# if __name__ == "__main__":
#     try:
#         sniff_DHCP(interface="eth0", count=0)
#     except Exception as e:
#         print("An error occurred:", e)
from scapy.all import sniff, DHCP

def DHCP_handler(packet):
    if DHCP in packet and packet[DHCP].options[0][1] == 1:  # Check if DHCP Discover
        print("DHCP Discover Packet Found")
        print(packet)

def sniff_DHCP(interface: "eth0", count: 0):
    print(f"Discovering the DHCP packet on {interface}")
    sniff(iface=interface, filter="udp and (port 67 or port 68)", prn=DHCP_handler, count=count)

if __name__ == "__main__":
    try:
        sniff_DHCP(interface="eth0", count=0)
    except Exception as e:
        print("An error occurred:", e)
