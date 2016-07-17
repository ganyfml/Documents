#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import sys
from prompt_toolkit import prompt

a = ''
for line in sys.stdin:
	a += line
print 'stdin is ' + a
b = prompt(u"Input: ")
