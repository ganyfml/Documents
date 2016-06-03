#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

a = {'a':1, 'b':2}
print [key for key in a]
print [(key, value) for key, value in a.items()]
