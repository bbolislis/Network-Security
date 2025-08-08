from scapy.all import IP, TCP, sniff

# sniff a packet
packet = sniff(count=1)[0]

# check if the packet contains an IP layer
if IP in packet:
  # print the fields of the IP layer with "ls()" method
  packet[IP].ls()

# check if the packet contains a TCP layer
if TCP in packet:
  # print the fields of the TCP layer
  packet[TCP].ls()