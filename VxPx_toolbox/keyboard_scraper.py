"""using scapy to try pull HID data from a pcap file and read it out in order. re-assembling the keyboard input"""
from scapy.all import *

packets = rdpcap("capture.pcapng")

print(hex(packets[0].show()))