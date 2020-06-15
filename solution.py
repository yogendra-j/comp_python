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
    x = int(inp())
    if x == -1:
        exit()
    return x


def det_mat(mat, r1, c1, r2, c2, inf):
    if (r2 - r1 + 1) * (c2 - c1 + 1) == inf:
        for _ in range(r2 - r1 + 1):
            mat[r1 + _][c1: c2 + 1] = ['1'] * (c2 - c1 + 1)
        return
    elif inf == 0:
        return
    if (r2 - r1 + 1) >= (c2 - c1 + 1):
        inf_ = query(r1, c1, r1 + (r2 - r1 + 1) // 2 - 1, c2)
        det_mat(mat, r1, c1, r1 + (r2 - r1 + 1) // 2 - 1, c2, inf_)
        det_mat(mat, r1 + (r2 - r1 + 1) // 2, c1, r2, c2, inf - inf_)
    else:
        inf_ = query(r1, c1, r2, c1 + (c2 - c1 + 1) // 2 - 1)
        det_mat(mat, r1, c1, r2, c1 + (c2 - c1 + 1) // 2 - 1, inf_)
        det_mat(mat, r1, c1 + (c2 - c1 + 1) // 2, r2, c2, inf - inf_)


T = int(inp())

for _ in range(T):
    N, p = map(int, inp().split())
    mat = [['0'] * N for _ in range(N)]
    Q = 5*N**2
    inf = query(0, 0, N - 1, N - 1)
    det_mat(mat, 0, 0, N - 1, N - 1, inf)
    print('2')
    for row in mat:
        pri(" ".join(row) + '\n')
    corr = int(inp())
    if corr == -1:
        exit()
    else:
        continue
