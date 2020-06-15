import sys
#-----------------------------------------------------------------------------#
# comment before submission
sys.stdin = open('inputs.txt', 'r')
sys.stdout = open('output.txt', 'w')
#-----------------------------------------------------------------------------#
input = sys.stdin.readline
print = sys.stdout.write

x = int(input())
print('NO' if x & 1 or x <= 2 else 'YES')
