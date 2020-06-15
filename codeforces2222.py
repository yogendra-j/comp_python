# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:07:48 2020

@author: yogendra jaiswal
"""


n = int(input())
 
a = list(map(int, input().split()))
x = max(a)

out = 1
i = 1
x = x//2
while x:
    out += 2**i
    x //= 2**(i)
    i += 1
    
print(out)
