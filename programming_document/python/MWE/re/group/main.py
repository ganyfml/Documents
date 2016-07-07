#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import re

r = re.search('a(.)', 'ab ')
print len(r.group())
print r.group(0)
print r.group(1)
print r.group(0, 1)

r = re.search('(?P<first>a)(?P<second>.)', 'ab ')
print r.group('first')
print r.group('second')
