# https://codeforces.com/problemset/problem/275/A

import sys
#-----------------------------------------------------------------------------#
try:
    sys.stdin = open('inputs.txt', 'r')
    sys.stdout = open('output.txt', 'w')
except:
    pass
finally:
    input = sys.stdin.readline
    print = sys.stdout.write

#-----------------------------------------------------------------------------#

lights = [[1] * 3 for _ in range(3)]
toggle = []

for r in range(3):

    toggle.append(list(map(int, input().split())))

for r in range(3):
    for c in range(3):
        toggles = toggle[r][c]
        if r > 0:
            toggles += toggle[r-1][c]
        if r < 2:
            toggles += toggle[r+1][c]
        if c > 0:
            toggles += toggle[r][c-1]
        if c < 2:
            toggles += toggle[r][c+1]
        if toggles & 1:
            lights[r][c] = 0
    print("".join(list(map(str, lights[r]))))
    print('\n')
