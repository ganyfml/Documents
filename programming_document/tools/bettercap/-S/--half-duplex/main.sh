#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

#Classic ARP attach with half duplex
sudo bettercap --half-duplex

#full duplex ICMP attach
sudo bettercap -S ICMP --half-duplex
