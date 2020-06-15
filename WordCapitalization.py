# https://codeforces.com/problemset/problem/281/A

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
word = list(input())
word[0] = word[0].upper()
print("".join(word))
