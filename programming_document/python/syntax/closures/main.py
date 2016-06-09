#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

#http://www.shutupandship.com/2012/01/python-closures-explained.html

def generate_power_func(n):
    print "id(n): %X" % id(n)
    def nth_power(x):
        return x**n
    print "id(nth_power): %X" % id(nth_power)
    return nth_power

raised_to_4 = generate_power_func(4)
del generate_power_func
print raised_to_4.__closure__
print raised_to_4.__closure__[0].cell_contents
