class Solution(object):
    def maxSumTrionic(self, nums):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Identify all strictly increasing segments
        inc = [0] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        # Identify all strictly decreasing segments
        dec = [0] * n
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                dec[i] = dec[i - 1] + 1

        max_sum = float('-inf')

        for q in range(1, n - 1):
            d = dec[q]
            if d == 0:
                continue

            p = q - d
            i_len = inc[p]
            if i_len == 0:
                continue

            l = p - i_len
            if l < 0:
                continue

            # check increasing again after q
            if q + 1 >= n or nums[q + 1] <= nums[q]:
                continue
            r = q + 1
            while r + 1 < n and nums[r + 1] > nums[r]:
                r += 1

            if l < p < q < r:
                total = prefix[r + 1] - prefix[l]
                max_sum = max(max_sum, total)

        return max_sum


print(Solution().maxSumTrionic([2, 993, -791, -635, -569]))
#  Output: -431
