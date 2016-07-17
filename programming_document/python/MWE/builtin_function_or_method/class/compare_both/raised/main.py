#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

# OK, old:
class Old: pass
try:
    raise Old()
except Old:
    pass
else:
    assert False

# TypeError, new not derived from `Exception`.
class New(object): pass
try:
    raise New()
except TypeError:
    pass
else:
    assert False

# OK, derived from `Exception`.
class New(Exception): pass
try:
    raise New()
except New:
    pass
else:
    assert False

# `'str'` is a new style object, so you can't raise it:
try:
    raise 'str'
except TypeError:
    pass
else:
    assert False
