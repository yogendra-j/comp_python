# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:17:58 2020

@author: yogendra jaiswal
"""


n = int(input())

sb = []
scores = {}

for i in range(n):
    
    name, score = input().split()
    sb.append([name, int(score)])
    if name in scores:
        scores[name] += int(score)
    
    else:
        scores[name] = int(score)

max_score = -2000
max_scorers = []

for name, score in scores.items():
    
    if score > max_score:
        max_scorers = [name]
        max_score = score
        
    elif score == max_score:
        max_scorers.append(name)

scores2 = {}
max_scorers = set(max_scorers)

for name, score in sb:
    if name not in max_scorers:
        continue
    if name in scores2:
        scores2[name] += score
        
    else:
        scores2[name] = score
    
    if scores2[name] >= max_score:
            print(name)
            break
        
    