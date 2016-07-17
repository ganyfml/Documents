#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

test_list = [1]

try:
	print test_list[1000]
except (ValueError, IndexError):
	print 'Invalid index'
