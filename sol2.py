# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 21:23:49 2020

@author: yogendra jaiswal
"""

from sys import stdin, stdout, exit

inp = stdin.readline
pri = stdout.write


def query(r1, c1, r2, c2):

    global Q
    Q -= 1
    if Q == 0:
        exit()
    print(1, r1 + 1, c1 + 1, r2 + 1, c2 + 1)
    x = inp()
    if int(x) == -1:
        exit()
    return x

T = int(inp())

for _ in range(T):
    N, p = map(int, inp().split())
    mat = [['0'] * N for _ in range(N)]
    Q = 5*N**2
    
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            mat[row][col] = query(row, col, row, col).strip()
            
    print('2')
    for row in mat:
        pri(" ".join(row) + '\n')
    x = int(inp())
    if x == 1:
        continue
    else:
        exit()
