# class Solution(object):
#     def countHillValley(self, nums):
#         if not nums or len(nums) < 3:
#             return 0

#         count = 0

#         for i in range(1, len(nums) - 1):
#             # Skip if nums[i] == nums[i-1], since it can't be a peak/valley start
#             if nums[i] == nums[i - 1]:
#                 continue

#             # Find previous non-equal to the left
#             left = i - 1
#             while left >= 0 and nums[left] == nums[i]:
#                 left -= 1

#             # Find next non-equal to the right
#             right = i + 1
#             while right < len(nums) and nums[right] == nums[i]:
#                 right += 1

#             # If either side doesn't have a non-equal neighbor, skip
#             if left < 0 or right >= len(nums):
#                 continue

#             # Now compare with the closest non-equal neighbors
#             if nums[i] > nums[left] and nums[i] > nums[right]:
#                 count += 1  # Hill
#             elif nums[i] < nums[left] and nums[i] < nums[right]:
#                 count += 1  # Valley

#         return count



# nums = [2, 4, 1, 1, 6, 5]
# print(Solution().countHillValley(nums))



#  printable 

class Solution(object):
    def countHillValley(self, nums):
        if not nums or len(nums) < 3:
            return 0

        count = 0

        for i in range(1, len(nums) - 1):
            print(f"\n Checking index {i}, value = {nums[i]}")
            if nums[i] == nums[i - 1]:
                print(f"  Skipped: nums[{i}] == nums[{i - 1}] == {nums[i]}")
                continue

            # Find closest non-equal to the left
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            # Find closest non-equal to the right
            right = i + 1
            while right < len(nums) and nums[right] == nums[i]:
                right += 1

            # Safety check
            if left < 0 or right >= len(nums):
                print("  Skipped: no non-equal neighbor on one side")
                continue

            print(f"  Neighbors: left = nums[{left}] = {nums[left]}, right = nums[{right}] = {nums[right]}")
            if nums[i] > nums[left] and nums[i] > nums[right]:
                print("   Hill found")
                count += 1
            elif nums[i] < nums[left] and nums[i] < nums[right]:
                print("   Valley found")
                count += 1
            else:
                print("   Not a hill or valley")

        print(f"\n Final count: {count}")
        return count


nums = [3, 3, 3, 3, 3]
print("\nTest Case 1: All equal")
Solution().countHillValley(nums)

nums = [1, 2, 2, 2, 1]
print("\nTest Case 2: Flat hill")
Solution().countHillValley(nums)

nums = [1, 3, 1, 3, 1, 3, 1]
print("\nTest Case 3: Alternating")
Solution().countHillValley(nums)

nums = [10, 5, 10]
print("\nTest Case 4: Valley in middle")
Solution().countHillValley(nums)

nums = [1] + [2]*100 + [1]
print("\nTest Case 5: Large flat hill")
Solution().countHillValley(nums)



nums = []
print("\nTest Case 6a: Empty list")
Solution().countHillValley(nums)

nums = [1]
print("\nTest Case 6b: Single element")
Solution().countHillValley(nums)

nums = [1, 2]
print("\nTest Case 6c: Two elements")
Solution().countHillValley(nums)
