from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        last_seen = [-1] * 30  # last seen index of bit i
        
        for i in range(n - 1, -1, -1):
            # Update last seen positions of each bit in nums[i]
            for bit in range(30):
                if (nums[i] >> bit) & 1:
                    last_seen[bit] = i
            
            # Find farthest bit index we must include
            max_index = i
            for j in range(30):
                if last_seen[j] != -1:
                    max_index = max(max_index, last_seen[j])
            
            answer[i] = max_index - i + 1
        
        return answer

# Example test case
nums = [1, 0, 2, 1, 3]
sol = Solution()
print(sol.smallestSubarrays(nums))  # Output: [3, 3, 2, 2, 1]
# Example test case
nums1 = [1, 2]
sol = Solution()
print(sol.smallestSubarrays(nums1))  # Output: [3, 3, 2, 2, 1]
