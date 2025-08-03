class Solution(object):
    def maximumMedianSum(self, nums):
        nums.sort()  
        n = len(nums)
        k = n // 3
        total = 0
    
        # Pick every second number from the last 2k elements
        # These are the best possible medians
        # The loop picks every second element from the back, starting 2nd last, to extract the k best medians (middle of biggest triplets).
        for i in range(n - 2, n - 2 * k - 1, -2):
            total += nums[i]
    
        return total
    

