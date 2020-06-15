# https://codeforces.com/problemset/problem/59/A

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

word = input().strip()

lc = 0
for ch in word:
    if ch.islower():
        lc += 1
    else:
        lc -= 1

if lc >= 0:
    print(word.lower())
else:
    print(word.upper())
