#!/usr/bin/env python
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

class myclass(object):
	a = []
	def __init__(self):
		pass
	def set_a(self,a):
		self.a.append(a)

i1 = myclass()
print id(i1.a)
print id(myclass.a)
print id(i1.set_a)
print id(myclass.set_a)
