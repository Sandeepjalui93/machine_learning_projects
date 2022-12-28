# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:41:53 2020

@author: SANDEEP
"""

import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'AT':10, 'V':40, 'AP':1000, 'RH':70})

print(r.json())