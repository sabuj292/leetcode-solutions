class Solution(object):
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        i = 0
        max_len = 0
        
        for j in range(n):
            while nums[j] > nums[i] * k:
                i += 1
            max_len = max(max_len, j - i + 1)
        
        return n - max_len

