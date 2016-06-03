#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

##MRO (Method Resolution Order) changed
#Old
class C: i = 0
class C1(C): pass
class C2(C): i = 2
class C12(C1, C2): pass
class C21(C2, C1): pass

assert C12().i == 0
assert C21().i == 2

try:
    C12.__mro__
except AttributeError:
    pass
else:
    assert False

#New
class C(object): i = 0
class C1(C): pass
class C2(C): i = 2
class C12(C1, C2): pass
class C21(C2, C1): pass

assert C12().i == 2
assert C21().i == 2

assert C12.__mro__ == (C12, C1, C2, C, object)
assert C21.__mro__ == (C21, C2, C1, C, object)
