import scapy.all as scapy
import subprocess
import os
colors = {'HEADER' : "\033[95m",
    'OKBLUE' : "\033[94m",
    'RED' : "\033[91m",
    'YELLOW' : "\033[93m",
    'GREEN' : "\033[92m",
    'LIGHTBLUE' : "\033[96m",
    'FAIL' : "\033[91m",
    'END' : "\033[0m",
    'BOLD' : "\033[1m",
    'UNDERLINE' : "\033[4m" }
print(colors["GREEN"]+"    _                      ____                     _ ")
print(colors["LIGHTBLUE"]+"   / \   _ __ _ __        / ___|_   _  __ _ _ __ __| |")
print(colors["RED"]+"  / _ \ | '__| '_ \ _____| |  _| | | |/ _` | '__/ _` |")
print(colors["GREEN"]+" / ___ \| |  | |_) |_____| |_| | |_| | (_| | | | (_| |")
print(colors["YELLOW"]+"/_/   \_\_|  | .__/       \____|\__,_|\__,_|_|  \__,_|")
print(colors["RED"]+"             |_|                                      ")
print(colors["LIGHTBLUE"]+"-"*70)
print(colors["GREEN"]+"          GITHUB:https://www.github.com/AzizKpln")
print(colors["GREEN"]+"          INSTAGRAM:https://www.instagram.com/aziz.kpln/")
print(colors["GREEN"]+"          FACEBOOK:https://www.facebook.com/aziz.kaplan.96387")
print(colors["LIGHTBLUE"]+"-"*70)
ipconfig=subprocess.check_output(["dmesg"])
ipconfig=ipconfig.decode("utf-8")
if "wlan0" in ipconfig:
    ipconfig_results=subprocess.check_output(["ifconfig","wlan0"])
    interface="wlan0"
elif "eth0" in ipconfig:
    ipconfig_results=subprocess.check_output(["ifconfig","eth0"])
    interface="eth0"
def get_mac(ip):
    request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    answered=scapy.srp(broadcast/request,timeout=1,verbose=False)[0]
    return answered[0][1].hwsrc
def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)
def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op==2:
        try:
            real_mac=get_mac(packet[scapy.ARP].psrc)
            response_mac=packet[scapy.ARP].hwsrc
            if real_mac!=response_mac:
                print(colors["BOLD"]+colors["RED"]+"[!][!][!]Arp Spoof Detected"+colors["END"])
                print(colors["YELLOW"]+colors["BOLD"]+"[+]INTERNET IS SHUTTING DOWN")
                network_manager="service network-manager stop"
                interface_down="ifconfig %s down"%interface
                os.system(network_manager)
                os.system(interface_down)
        except:
            pass
sniff(interface)