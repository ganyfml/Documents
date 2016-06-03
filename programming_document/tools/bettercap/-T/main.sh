#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

#Attack specific targets:
sudo bettercap -T 192.168.1.10,192.168.1.11

#Attack a specific target by its MAC address:
sudo bettercap -T 01:23:45:67:89:10

#Attack a range of IP addresses:
sudo bettercap -T 192.168.1.1-30

#Attack a specific subnet:
sudo bettercap -T 192.168.1.1/24

#Attack all the subnet
sudo bettercap
