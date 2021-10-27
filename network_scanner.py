#two parts mainly arp request and arp response
import scapy.all as scapy
def scan(ip):
    arp_request = scapy.ARP()
    print(arp_request.summary)
    scapy.ls(scapy.ARP)

    # scapy.arping(ip)
scan("192.168.133.2/24")   #just a boardcast request who has this called arp request

