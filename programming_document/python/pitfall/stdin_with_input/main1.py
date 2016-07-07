#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import sys
from prompt_toolkit import prompt

a = ''
with open(sys.argv[1]) as f:
	for line in f:
		a += line
print 'stdin is ' + a
b = prompt(u"Input: ")
