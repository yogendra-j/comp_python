# https://codeforces.com/problemset/problem/69/A
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

resultant = [0]*3

for _ in range(n):

    f = list(map(int, input().split()))

    resultant = [resultant[i] + f[i] for i in range(3)]

if resultant[0] == resultant[1] == resultant[2] == 0:
    print('YES')

else:
    print('NO')
