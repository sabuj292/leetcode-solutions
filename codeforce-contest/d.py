import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    total = 0
    
    # Precompute for efficiency
    for i in range(n):
        # For subarray starting at i, track max LDS as we extend
        max_lds = 0
        
        for j in range(i, n):
            # Calculate LDS ending at j in subarray [i, j]
            lds_at_j = 1
            
            for k in range(i, j):
                if p[k] > p[j]:
                    # This is inefficient, but let's see if basic optimizations help
                    temp_lds = 1
                    for m in range(i, k + 1):
                        if m == k:
                            temp_lds = max(temp_lds, lds_cache.get((i, k), 1))
                            break
                    lds_at_j = max(lds_at_j, temp_lds + 1)
            
            max_lds = max(max_lds, lds_at_j)
            total += max_lds
    
    return total

# Let me try a cleaner, simpler approach
def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    result = 0
    
    for i in range(n):
        dp = [1] * (n - i)  # dp for subarray starting at i
        
        for j in range(1, n - i):  # j is relative index from i
            for k in range(j):  # k is also relative index from i
                if p[i + k] > p[i + j]:  # Decreasing condition
                    dp[j] = max(dp[j], dp[k] + 1)
        
        # Add LDS lengths for all subarrays starting at i
        for j in range(n - i):
            # LDS of subarray [i, i+j] is max(dp[0:j+1])
            max_lds = max(dp[:j+1])
            result += max_lds
    
    return result

def main():
    t = int(input())
    for _ in range(t):
        print(solve())

if __name__ == "__main__":
    main()