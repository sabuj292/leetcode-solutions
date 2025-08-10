# Arboris Contractio


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    deg = [0]*(n+1)
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = map(int, input().split())
        adj[u].append(v); adj[v].append(u)
        deg[u]+=1; deg[v]+=1

    if n <= 2:
        print(0)
        continue

    # count leaves
    is_leaf = [False]*(n+1)
    leaves = []
    for i in range(1, n+1):
        if deg[i] == 1:
            is_leaf[i] = True
            leaves.append(i)
    L = len(leaves)

    # count leaf neighbors per node
    best = 0
    for u in range(1, n+1):
        c = 0
        for v in adj[u]:
            if is_leaf[v]:
                c += 1
        if c > best:
            best = c

    print(L - best)