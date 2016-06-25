#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set noexpandtab tabstop=2 shiftwidth=2 softtabstop=-1 fileencoding=utf-8:

import requests

proxies = {
		'http' : '218.202.111.10:80'
		}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

a = requests.get('http://www.whatismyip.com/', proxies = proxies, headers = headers)
print a.text.encode('utf-8')
