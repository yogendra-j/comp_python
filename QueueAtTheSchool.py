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

n, t = map(int, input().split())
q = list(input().strip())
for _ in range(t):
    i = 0
    while i < n - 1:

        if q[i] == 'B' and q[i + 1] == 'G':

            q[i], q[i + 1] = q[i + 1], q[i]
            i += 1
        i += 1

print("".join(q))
