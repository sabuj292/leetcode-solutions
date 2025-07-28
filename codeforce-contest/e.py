import sys
input = sys.stdin.readline

def solve_case(n, k, a):
    def check(x):
        b = [1 if ai >= x else -1 for ai in a]
        prefix = [0]
        for val in b:
            prefix.append(prefix[-1] + val)

        min_prefix = float('inf')
        for i in range(k, n + 1):
            min_prefix = min(min_prefix, prefix[i - k])
            if prefix[i] > min_prefix:
                return True
        return False

    # Binary search on possible submedian values
    lo, hi = 1, n
    ans = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    # Now find a valid subarray where ans is a median
    b = [1 if ai >= ans else -1 for ai in a]
    prefix = [0]
    for val in b:
        prefix.append(prefix[-1] + val)

    min_prefix = prefix[0]
    min_index = 0
    for i in range(k, n + 1):
        if prefix[i] - min_prefix > 0:
            # Subarray from min_index+1 to i (1-based)
            return ans, min_index + 1, i
        if prefix[i - k + 1] < min_prefix:
            min_prefix = prefix[i - k + 1]
            min_index = i - k + 1

    # fallback
    return ans, 1, k

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        val, l, r = solve_case(n, k, a)
        print(f"{val} {l} {r}")

if __name__ == "__main__":
    main()
