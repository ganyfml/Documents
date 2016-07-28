#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import sys

sys.stderr.write("Error!\n")

log = sys.stderr.write
log('Error!\n')

print >> sys.stderr, 'Error!\n'
