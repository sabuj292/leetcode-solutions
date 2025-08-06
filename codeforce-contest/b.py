t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 0, n - 1
    min_val, max_val = 0, n + 1
    ans = []
    
    while l <= r:
        if a[l] < max_val and a[l] > min_val:
            ans.append('L')
            max_val = a[l]
            l += 1
        elif a[r] < max_val and a[r] > min_val:
            ans.append('R')
            max_val = a[r]
            r -= 1
        else:
            # Any is valid — just take one that doesn't break range
            if a[l] < max_val:
                ans.append('L')
                max_val = a[l]
                l += 1
            else:
                ans.append('R')
                max_val = a[r]
                r -= 1
    print("".join(ans))
