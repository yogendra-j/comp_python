# https://codeforces.com/problemset/problem/148/A
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

kth = [int(input()) for _ in range(4)]

d = int(input())

dragons_hit = [0] * (d + 1)

for k in kth:

    for i in range(k, d + 1, k):
        dragons_hit[i] = 1

count = 0
for hit in dragons_hit:
    if hit == 1:
        count += 1
print(str(count))
