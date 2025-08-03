from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
        # Group all `u` values by their `v` endpoint
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        # Base score
        ans = 0 
        # `left` stores [top1, top2] `u` values seen so far, where top1 >= top2.
        # `left[0]` acts as our running `forbidden_start`.
        left = [0, 0] 
        # `bonus[u]` accumulates the total gain if the critical conflict involving `u` is removed.
        bonus = [0] * (n + 1)
        
        # Single pass from r = 1 to n
        for r in range(1, n + 1):
            # Check for new conflicts ending at `r` and update `left`
            for l in right[r]:
                # This is a concise trick to update the top two seen values
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            
            # Add the count for this endpoint to the base score
            ans += r - left[0]

            # The gain at this step is the difference between the top two forbidden starts.
            # We add this gain to the tally for the `u` value causing the restriction (`left[0]`).
            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        
        # The final result is the base score plus the maximum possible gain.
        return ans + max(bonus)
    
    
    
    # Assume Solution class is already defined above

sol = Solution()

# Test Case 1: Basic case
n1 = 4
conflicts1 = [[2, 3], [1, 4]]
print("Test 1 Output:", sol.maxSubarrays(n1, conflicts1))  # Expected: 9

# Test Case 2: Overlapping conflicts
n2 = 5
conflicts2 = [[1, 2], [2, 5], [3, 5]]
print("Test 2 Output:", sol.maxSubarrays(n2, conflicts2))  # Expected: 12

# Test Case 3: No conflicts at all
n3 = 6
conflicts3 = []
print("Test 3 Output:", sol.maxSubarrays(n3, conflicts3))  # Expected: 21

# Test Case 4: Completely disjoint pairs
n4 = 6
conflicts4 = [[1, 2], [3, 4], [5, 6]]
print("Test 4 Output:", sol.maxSubarrays(n4, conflicts4))  # Expected: 18

# Test Case 5: Long chain of conflicts
n5 = 6
conflicts5 = [[1, 6], [1, 5], [1, 4], [1, 3]]
print("Test 5 Output:", sol.maxSubarrays(n5, conflicts5))  # Expected: likely around 15-16

# Test Case 6: Minimum possible values
n6 = 2
conflicts6 = [[1, 2]]
print("Test 6 Output:", sol.maxSubarrays(n6, conflicts6))  # Expected: 3

# Test Case 7: Larger input (performance test)
n7 = 10000
conflicts7 = [[i, i + 1] for i in range(1, 10000)]
print("Test 7 Output:", sol.maxSubarrays(n7, conflicts7))  # Should not timeout
