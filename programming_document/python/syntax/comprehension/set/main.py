#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

a = {1, 2, 3, 4}
b = {x + 1 for x in a}
print b

a = {1, 2, 3, 4}
b = {2, 3, 4, 6}
c = {(x, y) for x in a for y in b if x + y == 7}
print c
d = {(x, y) for x in a for y in b}
print d

e = {x + 1 for x in range(5)}
print e
print list(e)
