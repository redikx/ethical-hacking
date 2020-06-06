#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC")
parser.add_option("-m", "--mac", dest="new_mac", help="New Mac of interface")
(option, argument) = parser.parse_args()

interface = option.interface;
new_mac = option.new_mac;

print("Interface " + interface + " changing MAC to " + new_mac + " ...")
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
subprocess.call(["ifconfig",interface])
