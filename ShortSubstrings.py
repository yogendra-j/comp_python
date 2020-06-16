# https://codeforces.com/contest/1367/problem/0
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

t = int(input())

for _ in range(t):

    b = input().strip()
    a = []

    for i in range(0, len(b), 2):
        a.append(b[i])
    a.append(b[-1])
    a.append('\n')

    print("".join(a))
