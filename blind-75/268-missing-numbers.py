
# not an optimal approach Brute Force attempt
class Solution(object):
    def missingNumber(self, nums):
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i
            

# Sum Formula trick

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = n * (n + 1) / 2
        return total - sum(nums)