class Solution:
    def countMaxOrSubsets(self, nums):
        from itertools import combinations

        n = len(nums)
        max_or = 0

        # Step 1: Find the maximum OR of any subset
        for i in range(1, 1 << n):
            curr_or = 0
            for j in range(n):
                if i & (1 << j):
                    curr_or |= nums[j]
            max_or = max(max_or, curr_or)

        # Step 2: Count subsets that give max OR
        count = 0
        for i in range(1, 1 << n):
            curr_or = 0
            for j in range(n):
                if i & (1 << j):
                    curr_or |= nums[j]
            if curr_or == max_or:
                count += 1

        return count


sol = Solution()
print(sol.countMaxOrSubsets([3, 2, 1, 5]))  # Output: 6
