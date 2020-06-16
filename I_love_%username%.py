# https://codeforces.com/problemset/problem/155/A
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

points = list(map(int, input().split()))

max_p = points[0]
min_p = points[0]
amazing_count = 0

for point in points:

    if point > max_p:
        amazing_count += 1
        max_p = point

    elif point < min_p:
        amazing_count += 1
        min_p = point

print(str(amazing_count))
