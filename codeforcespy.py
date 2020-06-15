# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:04:26 2020

@author: yogendra jaiswal
"""


t = int(input())

for _ in range(t):
    n = int(input())
    
    nums = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if sorted(nums) == nums:
        out = 'Yes'
    else:
        if len(set(b)) == 1:
            out = 'No'
        else:
            out = 'Yes'
    print(out)
    
    