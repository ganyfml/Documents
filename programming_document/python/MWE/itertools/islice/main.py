#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import itertools

a = [1, 2, 3, 4, 5]
print a
print [item for item in itertools.islice(a, 2)]

b = xrange(100)
print b
print [item for item in itertools.islice(b, 2)]
