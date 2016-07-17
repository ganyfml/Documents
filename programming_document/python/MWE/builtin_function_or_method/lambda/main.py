#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

f = lambda x: x**2
print f(2)

a = lambda x: True if x % 2 == 0 else False
print a(2)

print (lambda x: x+1)(2)
