# Lever

import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    b = [int(next(it)) for _ in range(n)]
    surplus = sum(max(ai - bi, 0) for ai, bi in zip(a, b))
    out.append(str(surplus + 1))
print("\n".join(out))