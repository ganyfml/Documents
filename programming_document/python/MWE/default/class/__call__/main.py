#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

class test_class(object):
	def __call__(self, args):
		return 'called'

foo = test_class()
print callable(foo)
print foo('aa')
