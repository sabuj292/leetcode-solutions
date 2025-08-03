# class Solution(object):
#     def isTrionic(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         n = len(nums)
#         if n < 3:
#             return False

#         inc = [False]*n
#         dec = [False]*n
#         inc2 = [False]*n

#         # Compute increasing from left
#         for i in range(1, n):
#             if nums[i-1] < nums[i]:
#                 inc[i] = True
#                 if inc[i-1]:
#                     inc[i] = True
#                 else:
#                     inc[i-1] = True

#         # Compute decreasing middle
#         for i in range(n-2, -1, -1):
#             if nums[i] > nums[i+1]:
#                 dec[i] = True
#                 if dec[i+1]:
#                     dec[i] = True
#                 else:
#                     dec[i+1] = True

#         # Compute increasing from right
#         for i in range(n-2, -1, -1):
#             if nums[i] < nums[i+1]:
#                 inc2[i] = True
#                 if inc2[i+1]:
#                     inc2[i] = True
#                 else:
#                     inc2[i+1] = True

#         # Now try all valid (p, q)
#         for p in range(1, n-2):
#             if not inc[p]:
#                 continue
#             for q in range(p+1, n-1):
#                 if not dec[p+1] or not inc2[q+1]:
#                     continue
#                 return True

#         return False

class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        if n < 3:
            return False

        # We’ll try to find the p and q such that:
        # increasing → decreasing → increasing
        
        i = 0

        # Step 1: Find strictly increasing
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == 0 or i == n-1:
            return False
        p = i

        # Step 2: Find strictly decreasing
        while i+1 < n and nums[i] > nums[i+1]:
            i += 1
        if i == p or i == n-1:
            return False
        q = i

        # Step 3: Find strictly increasing again
        while i+1 < n and nums[i] < nums[i+1]:
            i += 1
        if i == n-1:
            return True
        return False


sol = Solution()
print(sol.isTrionic([4, 1, 5, 2, 3]))  # Should return False 
print(sol.isTrionic([1, 3, 5, 4, 2, 6]))  # Should return True 



    # test_cases = [
    #     ([1, 3, 5, 4, 2, 6], True),     # Example 1 - trionic
    #     ([2, 1, 3], False),             # Example 2 - not trionic
    #     ([1, 2, 3, 2, 1, 2, 3], True),  # long symmetric pattern
    #     ([5, 4, 3, 2, 1], False),       # strictly decreasing only
    #     ([1, 2, 1, 2, 1], False),       # up-down-up but not strictly in all parts
    #     ([1, 4, 7, 6, 3, 5, 9], True),  # valid increasing-decreasing-increasing
    #     ([1, 3, 2, 1, 2, 3], True),     # valid trionic
    #     ([1, 2, 3], False),             # increasing only
    #     ([3, 2, 1], False),             # decreasing only
    #     ([1, 5, 4, 2, 6, 7], True),     # same as sample, different pattern
    # ]

    # for i, (nums, expected) in enumerate(test_cases):
    #     result = is_trionic(nums)
    #     print(f"Test Case {i+1}: nums = {nums}")
    #     print(f"Expected: {expected}, Got: {result}")
    #     print(" Passed" if result == expected else " Failed", end="\n\n")
