#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import dis

def foo(arg1,arg2):
	#do something with args
	a = arg1 + arg2
	print a

print dis.dis(foo)
