# https://codeforces.com/problemset/problem/248/A
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

left_closed = 0
right_closed = 0

for _ in range(t):

    l, r = input().split()
    if l == '0':
        left_closed += 1
    if r == '0':
        right_closed += 1

total = (left_closed if (left_closed <= t // 2) else (t - left_closed)) + (
    right_closed if (right_closed <= t // 2) else (t - right_closed))

print(str(total))
