#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import re

e = re.compile('(\w+) (\w+)')

r1 = e.match('AAA BBB')
print r1.group(1)
print r1.group(2)

r2 = e.match('YYY ZZZ')
print r2.group(1)
print r2.group(2)
