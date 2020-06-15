# https://codeforces.com/problemset/problem/32/B

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

messege = input().strip()

decoder = {'.': 0, '-.': 1, '--': 2}
i = 0
while i < len(messege):

    if messege[i] == '.':
        print('0')
    if messege[i] == '-':
        i += 1
        if messege[i] == '-':
            print('2')
        else:
            print('1')
    i += 1
