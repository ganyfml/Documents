#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import re

r = 'abacadae'
re_iter = re.finditer('a.', r)

print re_iter.next().group()
print re_iter.next().group()
