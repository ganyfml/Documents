#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

##type() and __class__ changed
class old_class:
	pass

class new_class(object):
	pass

o1 = old_class()
print o1.__class__
print type(o1)

n1 = new_class()
print n1.__class__
print type(n1)
