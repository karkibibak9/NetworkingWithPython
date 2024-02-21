#importing Scapy
from scapy.all import Ether, sendp

#Creating Ethernet Frame
ether_Frame = Ether(dst="ff:ff:ff:ff:ff:ff", src="00:55:88:55:44")

print("Ethernet_Frame Summery:")
print(ether_Frame.summary())

#sending the Frame
sendp(ether_Frame, iface="eth0")