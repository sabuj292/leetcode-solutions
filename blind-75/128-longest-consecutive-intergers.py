"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        if not nums:
            return 0
        
        result = set()
        for i in range(0, len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                count += 1
            else:
                result.add(count)
                count = 1
        # adding the last streak
        result.add(count)
        return max(result)
        