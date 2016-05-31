#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v
#Not portable

#all to file
ls -abcdefg &> file.txt

#all to nowhere
ls -al &> /dev/null
