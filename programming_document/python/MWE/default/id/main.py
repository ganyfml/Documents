#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

i = 5
print id(i)
i = 6
print id(i)

l = []
print id(l)
l.append(5)
print id(l)
l = []
print id(l)
