#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v 
seq 3 | xargs -I {} echo 'aaa' {}

seq 3 | xargs -I args echo 'aaa' args
