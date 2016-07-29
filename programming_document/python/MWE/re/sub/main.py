#!/usr/bin/env python
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import re

ori_str = 'I am apple, and I like apple'
new_str = re.sub('apple', 'banana', ori_str)
print new_str
