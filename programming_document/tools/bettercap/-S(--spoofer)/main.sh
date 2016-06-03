#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

#Classic ARP attach
sudo bettercap
sudo bettercap -S ARP
sudo bettercap --spoofer ARP

#full duplex ICMP attach
sudo bettercap -S ICMP
sudo bettercap --spoofer ICMP
