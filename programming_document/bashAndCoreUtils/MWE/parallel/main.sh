#!/usr/bin/env bash
#vim: set noexpandtab tabstop=2:

#Run program in multithread

function cmd {
echo $1
}

#Export the function `cmd()` so that parallel can see
export -f cmd

printf '%s\n' {A..Z} | parallel 'cmd {}'
