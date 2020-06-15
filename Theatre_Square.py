# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:01:27 2020

@author: yogendra jaiswal
"""


from math import ceil

n, m, a = map(int, input().split())

print((ceil(n / a) * (ceil(m / a))))