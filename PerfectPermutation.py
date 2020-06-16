# https://codeforces.com/problemset/problem/233/A
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

n = int(input())

if n & 1:
    print(str(-1))

else:
    out = [str(i + 1) if i & 1 else str(i - 1) for i in range(1, n + 1)]
    print(" ".join(out))
