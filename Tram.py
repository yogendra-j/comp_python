# https://codeforces.com/problemset/problem/116/A
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
cap = 0
out = 0
in_ = 0

for _ in range(n):

    o, i = map(int, input().split())
    out += o
    in_ += i
    cap = max(cap, in_ - out)

print(str(cap))
