#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

#As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored

test_dict = {'a':1, 'b':2}
for __, value in test_dict.items():
	print value
