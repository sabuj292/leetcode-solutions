# Adjacent XOR

import sys

def possible(a, b):
    n = len(a)
    if a[-1] != b[-1]:
        return False
    for i in range(n - 2, -1, -1):
        if b[i] == a[i] or b[i] == (a[i] ^ a[i+1]) or b[i] == (a[i] ^ b[i+1]):
            continue
        return False
    return True


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES" if possible(a, b) else "NO")