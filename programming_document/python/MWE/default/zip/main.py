#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

a = [1, 2, 3, 4]
b = [4, 3, 5, 6]

z = zip(a, b)
print z

a1, b1 = zip(*z)
print a1
print b1

print list(a1) == a
print list(b1) == b
