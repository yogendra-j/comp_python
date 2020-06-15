# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 20:29:09 2020

@author: yogendra jaiswal
"""

col_map = {'a': 0, 'b': 1, 'c': 2,
           'd': 3, 'e': 4, 'f': 5,
           'g': 6, 'h': 7}

def index(cell):
        global col_map
        return (col_map[cell[0]], 8 - int(cell[1]))

s = input()
t = input()

s = index(s)
t = index(t)

step_map = {'L': (-1, 0), 'R': (1, 0),
            'U': (0, -1), 'D': (0, 1),
            'LU': (-1, -1), 'RU': (1, -1),
            'LD': (-1, 1), 'RD': (1, 1)}

def dist(s, t):
    return (s[0] - t[0]) ** 2 + (s[1] - t[1]) ** 2

def best_step(s, t):
    min_dis = 9999
    step_ = None
    for step, change in step_map.items():
        if dist((s[0] + change[0], s[1] + change[1]), t) < min_dis:
            min_dis = dist((s[0] + change[0], s[1] + change[1]), t)
            step_ = step
    return step_

curr_dis = dist(s, t)
steps = []

while curr_dis:
    step_ = best_step(s, t)
    change = step_map[step_]
    s = (s[0] + change[0], s[1] + change[1])
    steps.append(step_)
    curr_dis = dist(s, t)

print(len(steps))
for i in steps:
    print(i)
    
    