#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import matplotlib.pyplot as pyplot

a = range(10,20)
pyplot.hist(range(0,10), weights=a)
pyplot.show()
