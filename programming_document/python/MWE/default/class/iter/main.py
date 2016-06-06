#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

class test_class(object):
	def __init__(self):
		self.index = 0

	def __iter__(self):
		return self

	def next(self):
		if(self.index == 5):
			raise StopIteration
		else:
			self.index += 1
			return 'haha'

test_obj = test_class()
for s in test_obj:
	print s
