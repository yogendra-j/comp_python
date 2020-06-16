# https://codeforces.com/contest/1367/problem/B
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
t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    wrong_even = 0
    wrong_odd = 0

    for ind, num in enumerate(a):

        if ind & 1:
            if num & 1:
                pass
            else:
                wrong_odd += 1
        else:
            if num & 1:
                wrong_even += 1

    if wrong_even == wrong_odd:
        print(str(wrong_odd))
        print('\n')
    else:
        print('-1\n')
