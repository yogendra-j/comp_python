# https://codeforces.com/problemset/problem/6/A

import sys
#-----------------------------------------------------------------------------#
# # comment before submission
# sys.stdin = open('inputs.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#-----------------------------------------------------------------------------#
input = sys.stdin.readline
print = sys.stdout.write

sides = sorted(list(map(int, input().split())))

if sides[3] < sides[2] + sides[1] or sides[2] < sides[1] + sides[0]:
    print('TRIANGLE')

elif sides[3] == sides[2] + sides[1] or sides[2] == sides[1] + sides[0]:
    print('SEGMENT')

else:
    print('IMPOSSIBLE')
