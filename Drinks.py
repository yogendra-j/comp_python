# https://codeforces.com/problemset/problem/200/B
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

p = list(map(int, input().split()))

print(str(sum(p) / n))
