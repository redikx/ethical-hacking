#!/usr/bin/env python
# Script to change MAC address of specified interface
# -i,--interface : name of the interface (eth0)
# -m,--mac :       new MAC
#

import subprocess
import optparse

def get_parameters():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac of interface")
    options, argumemnts = parser.parse_args()
    if not options.interface:
        parser.error("Specify interface using -i or --inteface option")
    elif not options.new_mac:
        parser.error("Please specify new mac using -m or --mac")
    return options

def change_mac(interface,new_mac):
    print("[+] Interface " + interface + " changing MAC to " + new_mac + " ...")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

option = get_parameters()
change_mac(option.interface,option.new_mac)

subprocess.call("ifconfig " + option.interface  + " | grep ether",shell=True)
