#!/usr/bin/env python
# Script to change MAC address of specified interface


import optparse
import subprocess
import re

def get_parameters():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac of interface")
    options, arguments = parser.parse_args()
    if not options.interface:
        parser.error("Specify interface using -i or --inteface option")
    return options

def get_mac(interface):
    mac_check = subprocess.check_output(['ifconfig', interface]).decode()
    mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , mac_check)
    if mac:
        return mac.group(0)
    else:
        return "No MAC found"

def change_mac(interface, new_mac):
    print("Changing MAC of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig", interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def main():
    options = get_parameters()
    interface = options.interface
    mc_curr_addr = get_mac(interface)
    print("Current MAC is " + mc_curr_addr)
    if options.new_mac:
        new_mac = options.new_mac
        change_mac(interface,new_mac)
        mc_curr_addr = get_mac(interface)
        print("[+] New MAC is " + mc_curr_addr)

if __name__ == "__main__":
    main()