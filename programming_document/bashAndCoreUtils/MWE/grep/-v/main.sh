#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

set -v

find ../ -name "*cpp" 

find ../ -name "*cpp" | grep -v main
