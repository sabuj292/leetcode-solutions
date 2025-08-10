# Unjust Binary Life

import sys
import bisect

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input().strip())
    a = input().strip()
    b = input().strip()

    A1 = [0]*(n+1)
    B1 = [0]*(n+1)
    for i in range(1, n+1):
        A1[i] = A1[i-1] + (a[i-1] == '1')
        B1[i] = B1[i-1] + (b[i-1] == '1')

    sA = [0]*(n+1)
    sB = [0]*(n+1)
    for i in range(1, n+1):
        sA[i] = i - 2*A1[i]
        sB[i] = i - 2*B1[i]

    pairs = [(sB[i], B1[i], i - B1[i]) for i in range(1, n+1)]
    pairs.sort(key=lambda x: x[0])

    SB_sorted = [p[0] for p in pairs]
    pref_cnt = [0]*(n+1)
    pref_B1  = [0]*(n+1)
    pref_B0  = [0]*(n+1)
    for i in range(1, n+1):
        pref_cnt[i] = pref_cnt[i-1] + 1
        pref_B1[i]  = pref_B1[i-1] + pairs[i-1][1]
        pref_B0[i]  = pref_B0[i-1] + pairs[i-1][2]

    tot_B1 = pref_B1[n]
    tot_B0 = pref_B0[n]

    ans = 0
    for x in range(1, n+1):
        A1x = A1[x]
        A0x = x - A1x
        idx = bisect.bisect_left(SB_sorted, -sA[x])
        k = n - idx
        sum_B1_ge = tot_B1 - pref_B1[idx]
        sum_B0_lt = pref_B0[idx]
        ans += k * A1x + sum_B1_ge
        ans += (n - k) * A0x + sum_B0_lt

    print(ans)