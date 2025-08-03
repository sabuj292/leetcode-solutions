class Solution(object):
    def maxSumTrionic(self, nums):
        n = len(nums)

        # Step 1: Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Step 2: Build increasing and decreasing lengths
        incL = [0] * n  # Length of increasing subarray ending at i
        dec = [0] * n   # Length of decreasing subarray ending at i
        incR = [0] * n  # Length of increasing subarray starting at i

        # Compute increasing left
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                incL[i] = incL[i - 1] + 1
            else:
                incL[i] = 0

        # Compute decreasing center
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                dec[i] = dec[i - 1] + 1
            else:
                dec[i] = 0

        # Compute increasing right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                incR[i] = incR[i + 1] + 1
            else:
                incR[i] = 0

        max_sum = float('-inf')

        # Step 3: Try all valid q (center of the valley)
        for q in range(1, n - 1):
            p = q - dec[q]
            l = p - incL[p] if p - incL[p] >= 0 else -1
            r = q + incR[q]

            if l >= 0 and r < n and l < p < q < r:
                total = prefix[r + 1] - prefix[l]
                max_sum = max(max_sum, total)

        return max_sum

sol = Solution()
print(sol.maxSumTrionic([1, 4, 2, 7]))              # Output: 14
print(sol.maxSumTrionic([0, -2, -1, -3, 0, 2, -1]))  # Output: -4
