#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v 
echo $(seq 3)

seq 3 | xargs -r echo
