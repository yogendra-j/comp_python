# https://codeforces.com/problemset/problem/61/A
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

s1 = input().strip()
s2 = input().strip()
out = ['0']*len(s1)

for i in range(len(s1)):
    if s1[i] == s2[i]:
        pass
    else:
        out[i] = '1'

print("".join(out))
