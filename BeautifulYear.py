# https://codeforces.com/problemset/problem/271/A

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
year1 = int(input())

year2 = year1 + 1


def next_unq(year):

    count = set()
    for j, i in enumerate(year):
        if i in count:
            break
        else:
            count.add(i)
    else:
        return year

    year = str((int(year) // 10 ** (3 - j)) *
               10 ** (3 - j) + 10 ** (3 - j))

    return next_unq(year)


print(next_unq(str(year2)))
