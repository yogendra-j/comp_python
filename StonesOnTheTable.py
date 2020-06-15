# https://codeforces.com/problemset/problem/266/A
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
stones = input()
count = 0

for i in range(1, n):
    if stones[i] == stones[i-1]:
        count += 1
print(str(count))
