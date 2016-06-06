#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import re

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print m.group(1)
print m.group(2)

e = re.compile('(\w+) (\w+)')
r1 = e.match('AAA BBB')
print r1.group(1)
print r1.group(2)

print re.match(r"(\w+) (\w+)", "test\nIsaac Newton")
