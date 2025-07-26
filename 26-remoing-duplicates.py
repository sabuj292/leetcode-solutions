# Method 1

class Solution(object):
    def removeDuplicates(self, nums):
      
        if not nums:
            return 0

        i = 0  

        for j in range(1, len(nums)):  
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1  



# Method 2

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0

#         unique_index = 0  # pointer to last unique value

#         for i in range(1, len(nums)):
#             if nums[i] != nums[unique_index]:
#                 unique_index += 1
#                 nums[unique_index] = nums[i]

#         return unique_index + 1  # number of unique elements


#Method 3

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         unique_nums = []
#         count = 0
#         for num in nums:
#             if num in unique_nums:
#                 continue 
#             else:
#                 unique_nums.append(num)
#                 count += 1
                
#         nums[:len(unique_nums)] = unique_nums

#         return count