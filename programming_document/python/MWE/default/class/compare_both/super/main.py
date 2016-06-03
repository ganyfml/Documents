#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

##Old
class old_base: pass

class old_base_child(old_base):
    def __init__(self):
        old_base.__init__(self)

##New
class new_base(object): pass

class new_base_child(new_base):
    def __init__(self):
        super(new_base_child, self).__init__()
