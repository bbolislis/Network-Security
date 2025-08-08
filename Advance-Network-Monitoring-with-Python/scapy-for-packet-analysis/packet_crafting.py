from scapy.all import IP, UDP, DNS, DNSQR, send

# create an IP packet
ip = IP(dst="8.8.8.8")

# create a UDP packet
udp = UDP(dport=53)

# create a DNS query
dns = DNS(rd=1, qd=DNSQR(qname="example.com"))

# combine the layers
packet = ip/udp/dns

# send the packet
send(packet)