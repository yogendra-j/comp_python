# https://codeforces.com/problemset/problem/144/A
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
h = list(map(int, input().split()))

min_ind = 1
max_ind = 0

for i in range(n):
    if h[i] > h[max_ind]:
        max_ind = i
    elif h[i] <= h[min_ind]:
        min_ind = i

if min_ind < max_ind:
    print(str(max_ind + (n - 1) - min_ind - 1))
else:
    print(str((max_ind + (n - 1) - min_ind)))
