#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import re

print re.match(r"(\w+) (\w+)", "test\nIsaac Newton")

r = re.search(r"(\w+) (\w+)", "test\nIsaac Newton")
print r
print r.group(0)
print r.group(1)
print r.group(2)
