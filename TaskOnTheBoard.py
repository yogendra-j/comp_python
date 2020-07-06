import sys
te  # https://codeforces.com/contest/1367/problem/D
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

    s = input().strip()
    m = int(input())
    b = list(map(int, input().split()))

    alphas = [0] * 26

    for ch in s:
        alphas[ord(ch) - 97] += 1

    out = [0] * m
    z = set()
    alpha_no = 25
    a = []
    # print(str(alphas))

    while True:

        count = 0
        zs = []
        for j in range(m):
            if b[j] != 0:
                for zind in a:
                    b[j] -= abs(j - zind)

            if b[j] == 0 and j not in z:
                count += 1
                zs.append(j)
        # print(str(count))
        while alphas[alpha_no] < count:
            alpha_no -= 1

        for i in zs:
            out[i] = chr(alpha_no + 97)
            z.add(i)
        alpha_no -= 1
        a = zs
        if len(z) == m:
            break

    print("".join(out))
    print('\n')
