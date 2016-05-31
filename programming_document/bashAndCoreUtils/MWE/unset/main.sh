#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v 
export v=1
echo "$v"
bash -c 'echo $v'

unset v
echo "$v"
bash -c 'echo $v'
