class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
        
        
# Manual Solution


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False

        for i, value in enumerate(nums):
            if value == target:
                found = True
                return i
        if not found:
            return -1