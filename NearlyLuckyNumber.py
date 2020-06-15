# https://codeforces.com/problemset/problem/110/A
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

num = input()
count = 0

for ch in num:
    if ch in {'4', '7'}:
        count += 1
if count in {4, 7}:
    print('YES')
else:
    print('NO')
