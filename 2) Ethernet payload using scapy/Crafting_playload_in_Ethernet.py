from scapy.all import Ether, sendp, Raw

#asking user for payload
user_input = input("Enter Playload")

#Encoding the string to bytes
payload_data = user_input.encode()

#crafting Ethernet Frame with Payload
ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff", src="11:22:33:44:55:66")/Raw(load=payload_data)

#print
print("Ethernet Frame Summery")
print(ether_frame.summary())

sendp(ether_frame, iface="eth0")