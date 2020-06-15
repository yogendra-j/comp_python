# https://codeforces.com/problemset/problem/263/A

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

for row in range(1, 6):

    this_row = input().split()
    try:
        col = this_row.index('1')
        out = abs(row - 3) + abs(col - 2)
        print(str(out))
        break
    except:
        pass
