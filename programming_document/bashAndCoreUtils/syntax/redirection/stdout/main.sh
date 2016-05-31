#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v
#stdout to file
ls -l > file.txt

#stdout to stderr
ls -l 1>&2

#stdout to nowhere
ls -l > /dev/null
