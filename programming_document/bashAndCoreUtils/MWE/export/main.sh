#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v 
v=1
bash -c 'echo $v'

export v=2
bash -c 'echo $v'

unset v
