#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

test_list = [1,5,2,4]

print reduce(lambda x,y: x + y, test_list)
print reduce(lambda x,y: x if x > y else y, test_list)
