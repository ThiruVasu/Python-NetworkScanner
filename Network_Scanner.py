#!/usr/bin/env python

import scapy.all as scapy
import smtplib




def scan():
    print("*************************WELCOME TO MY NETWORK SCANNER*********************************")
    network_details = raw_input("ENTER THE NETWORK ADDRESS THAT HAS TO BE SCANNED---> ")
    request_packet = scapy.ARP()
    request_packet.pdst = network_details
    broadcast_mac = "ff:ff:ff:ff:ff:ff"
    broadcast_packet = scapy.Ether()
    broadcast_packet.dst = broadcast_mac
    final_packet = broadcast_packet/request_packet
    response_packet = scapy.srp(final_packet , timeout=1 , verbose = False)[0]
    new_list = []
    for packet in response_packet:
        dictionary = { "MAC" : packet[1].hwsrc , "IP" : packet[1].psrc}
        new_list.append(dictionary)
    return str(new_list)


def copytofile(filename , content):
    with open(filename, "wb") as file:
        file.write(content)
        print("scanning done successfully")

def sendmail(email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()


scan_result = scan()
savedata = raw_input("SCANNING DONE SUCCESSFULLY.DO YOU WANT TO SAVE IT TO LOCAL SYSTEM.ENTER YES OR NO---> ")
if savedata == "yes":
    copytofile("SCANRESULT", result)
elif savedata == "no":
    email = raw_input("WOULD YOU LIKE TO SEND IT TO YOUR EMAIL ADDRESS.ENTER YES OR NO---> ")
    if email == "yes":
        emailaddress = raw_input("ENTER THE EMAIL ADDRESS---> ")
        password = raw_input("ENTER THE PASSWORD---> ")
        sendmail(emailaddress, password, "\n\n" + scan_result)
        print("RESULT HAS BEEN EMAILED")
else:
    print("INVALID ENTRY")