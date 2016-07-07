#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

list1 = ['a']
list2 = list1
print id(list1)
print id(list2)

list3 = list4 = []
print id(list3)
print id(list4)

list5 = ['a']
list6 = list5[:]
print list5
print list5
print id(list5)
print id(list6)
