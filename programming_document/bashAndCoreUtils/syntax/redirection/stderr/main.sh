#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v
#stderr to file
ls -abcdefg 2> file.txt

#stderr to stdout
ls -abcdefg 2>&1

#stderr to nowhere
ls -abcdefg 2>/dev/null
