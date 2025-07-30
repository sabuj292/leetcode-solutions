
# the following solution is correct by will get "TLE" 


# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         for i in range(len(nums)):
#             if nums[i] in nums[i+1:]:
#                 return True
#         return False


# optimal method O(n)- TC

class Solution(object):
    def containDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num  in seen:
                return True
            seen.add(num)
        return False
    
    
    
# another way first sort then compare O(n^2)  - TC

# class Solution(object):
#     def containDuplicate(self, nums):
#         nums.sort()  # O(n log n)
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False





test_cases = [
    ([1, 2, 3, 4], False),               # No duplicates
    ([1, 2, 3, 1], True),                # One duplicate
    ([1, 1, 1, 1], True),                # All duplicates
    ([1], False),                       # Single element
    ([], False),                        # Empty list
    ([0, -1, -2, -3, 0], True),         # Zero duplicate
    ([1000000] * 100000, True),         # Large input (all same) - fast due to set
    (list(range(100000)), False),       # Large input, all unique
]

# ----------------------
#  Run and Print
# ----------------------

sol = Solution()

for i, (nums, expected) in enumerate(test_cases):
    result = sol.containDuplicate(nums)
    print(f"Test Case {i+1}: {nums[:10]}{'...' if len(nums) > 10 else ''}")
    print(f"  Expected: {expected}")
    print(f"  Got     : {result}")
    print(f"  {' PASS' if result == expected else ' FAIL'}\n")
