class Solution(object):
    def merge(self, nums1, m, nums2, n):
         """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
         i = m - 1 # last real index of nums1 excluding 0
         j = n - 1 # last index of nums2
         k = m + n - 1
         
         while j <= 0:
            if i >= 0 and nums1[i] > nums[j]:
                nums1[k] = nums1[i] 
                i -= 1
            else:
                nums1[k] = nums[j]
                j -= 1
            k -= 1
            
         
         