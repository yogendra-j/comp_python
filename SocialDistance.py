# https://codeforces.com/contest/1367/problem/C
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
    n, k = map(int, input().split())

    stiing = input().strip()

    count = 0
    i = 0
    one = [float('-inf')]
    while i < n:

        if stiing[i] == '1':
            one.append(i)
        else:
            if i - one[-1] > k:
                j = i
                while j <= i + k and j < n:
                    if stiing[j] == '1':
                        one.append(j)
                        i = j
                        break
                    j += 1
                else:
                    count += 1
                    one.append(i)
                    i = j - 1
        i += 1

    print(str(count))
    print('\n')
