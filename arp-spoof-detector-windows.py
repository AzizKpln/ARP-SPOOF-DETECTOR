import os
import subprocess
import time
from clint.textui import colored
import smtplib
print(colored.red("    _                      ____                     _ "))
print(colored.blue("   / \   _ __ _ __        / ___|_   _  __ _ _ __ __| |"))
print(colored.red("  / _ \ | '__| '_ \ _____| |  _| | | |/ _` | '__/ _` |"))
print(colored.green(" / ___ \| |  | |_) |_____| |_| | |_| | (_| | | | (_| |"))
print(colored.yellow("/_/   \_\_|  | .__/       \____|\__,_|\__,_|_|  \__,_|"))
print(colored.red("             |_|                                      "))
print(colored.blue("-"*70))
print(colored.green("          GITHUB:https://www.github.com/AzizKpln"))
print(colored.green("          INSTAGRAM:https://www.instagram.com/aziz.kpln/"))
print(colored.green("          FACEBOOK:https://www.facebook.com/aziz.kaplan.96387"))
print(colored.blue("-"*70))
def send_mail(e_mail,password,message):
    sw=smtplib.SMTP("smtp.gmail.com",587)
    sw.starttls()
    sw.login(e_mail,password)
    sw.sendmail(e_mail,e_mail,message)
    sw.quit()
def arp_spoof_detector():
    arp_mac_address_table=list()
    router_mac=""
    new_arp_table=list()
    check=subprocess.check_output(["arp","-a"])
    check=check.decode("utf-8")
    check=check.split(" ")
    for mac_address in check:
        if "-" in mac_address or ":" in mac_address and "Interface" not in mac_address and "---" not in mac_address:
            arp_mac_address_table.append(mac_address)
    router_mac=str(arp_mac_address_table[1])
    for i in arp_mac_address_table:
        if router_mac in i:
            pass
        else:
            new_arp_table.append(i)
    
    try:
        calc=2
        for j in arp_mac_address_table:
           
            if router_mac==arp_mac_address_table[calc]:
                print(colored.red("[!][!][!]ARP SPOOF DETECTED"))
                message="!!!!!!!!!ARP SPOOF DETECTED IN YOUR SYSTEM YOU ARE NOT SAFE\n!!!!!!!!!ARP SPOOF DETECTED IN YOUR SYSTEM YOU ARE NOT SAFE\n!!!!!!!!!ARP SPOOF DETECTED IN YOUR SYSTEM YOU ARE NOT SAFE\n!!!!!!!!!ARP SPOOF DETECTED IN YOUR SYSTEM YOU ARE NOT SAFE"
                send_mail(yourmailhere,yourpasswordhere,message)

                print(colored.green("[+]Mail Sent."))
                
                
            calc+=1
            
    except IndexError:
        pass
    
while True:
    arp_spoof_detector()
    time.sleep(1)
   
