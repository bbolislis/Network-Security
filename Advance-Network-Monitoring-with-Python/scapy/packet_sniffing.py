from scapy.all import sniff, IP

# take a packet as input and extract the source and destination IP addressess
def packet_callback(packet):
  if IP in packet:
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")

# sniff packets and call the packet_callback function for each packet
sniff(prn=packet_callback, count=10)