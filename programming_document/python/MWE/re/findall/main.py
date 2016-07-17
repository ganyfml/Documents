#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import re

r = 'ab ac ad ae'
re_all = re.findall('(a)(.)', r)

print len(re_all)
print re_all
