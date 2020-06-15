# https://codeforces.com/problemset/problem/80/A
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

n, m = map(int, input().split())


def primes(n, m):
    prime = [1 for i in range(0, m + 1)]
    for i in range(2, int((m ** 0.5) + 1)):
        j = 2
        while i * j < m:
            prime[i * j] = 0
            j += 1
        if i * j == m:
            return False
    for i in range(m - 1, n, -1):
        if prime[i] == 1:
            return False
    return True


if primes(n, m):
    print('YES')
else:
    print('NO')
