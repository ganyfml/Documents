#!/usr/bin/env python
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

class myclass(object):
	def __init__(self):
		self.a = 2
		self.b = []
		pass

i1 = myclass()
i2 = myclass()
print id(i1.a)
print id(i2.a)
print id(i1.b)
print id(i2.b)
