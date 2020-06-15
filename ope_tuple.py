from sys import stdin, stdout

inp = stdin.readline
pri = stdout.write

T = int(inp())

def max_allop(p, q):
    l = []
    for i in range(len(p)):
        if p[i] != q[i]:
            l.append((p[1], q[i]))
    return p, q, len(p)
    
for _ in range(T):
    p = map(int, inp().split())
    q = map(int, inp().split())
    
    while True:
        p, q, mop = max_allop(p, q) 
        
    

