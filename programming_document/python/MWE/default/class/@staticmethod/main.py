#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

class MyClass(object):
	@staticmethod
	def the_static_method(x):
		print x

MyClass.the_static_method(2)
