# https://codeforces.com/problemset/problem/9/A
import sys
#-----------------------------------------------------------------------------#
# comment before submission
# sys.stdin = open('inputs.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#-----------------------------------------------------------------------------#
input = sys.stdin.readline
print = sys.stdout.write


def hcf(x1, x2):
    x1, x2 = max(x1, x2), min(x1, x2)
    while x1 % x2:
        x1, x2 = x2, x1 % x2

    return x2


d1 = max(map(int, input().split()))
total_cases = 6
fav_cases = total_cases - d1 + 1

nume = fav_cases//hcf(fav_cases, total_cases)
deno = total_cases // hcf(fav_cases, total_cases)

print(f'{nume}/{deno}')
