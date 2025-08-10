# make it equal

import sys
from collections import Counter

def solve():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        S = [int(next(it)) for _ in range(n)]
        T = [int(next(it)) for _ in range(n)]

        cntS = Counter(x % k for x in S) if k != 0 else Counter({0: n})
        cntT = Counter(x % k for x in T) if k != 0 else Counter({0: n})

        ok = True
        seen = set()

        for r in set(cntS.keys()) | set(cntT.keys()):
            if r in seen: 
                continue
            r2 = (k - r) % k

            if r == r2:  # self-inverse residues: r=0 and (k even and r=k/2)
                if cntS.get(r, 0) != cntT.get(r, 0):
                    ok = False
                    break
                seen.add(r)
            else:
                totalS = cntS.get(r, 0) + cntS.get(r2, 0)
                totalT = cntT.get(r, 0) + cntT.get(r2, 0)
                if totalS != totalT:
                    ok = False
                    break
                seen.add(r); seen.add(r2)

        out.append("YES" if ok else "NO")
    print("\n".join(out))

if __name__ == "__main__":
    solve()