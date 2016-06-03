#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v

#stderr to file
ls -abcdefg 2> file.txt

#stdout to stderr
ls -l >&1

#position does not matter
>&1 ls -l

2>> file.txt ls -abcdefg
