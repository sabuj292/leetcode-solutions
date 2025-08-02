# class Solution(object):
#     def subarrayMajority(self, nums, queries):
#         """
#         :type nums: List[int]
#         :type queries: List[List[int]]
#         :rtype: List[int]
#         """
#         ©leetcode




from collections import defaultdict
import bisect
class Solution(object):
    def subarrayMajority(self,nums, queries):
        pos_map = defaultdict(list)
        freq_map = defaultdict(int)

        # Preprocessing
        for i, num in enumerate(nums):
            pos_map[num].append(i)
            freq_map[num] += 1

        result = []

        for l, r, threshold in queries:
            best = -1
            max_freq = threshold - 1  # Minimum frequency needed

            for num in freq_map:
                # Optimization: Only consider if possible to reach max_freq
                if freq_map[num] < threshold:
                    continue

                pos_list = pos_map[num]
                left = bisect.bisect_left(pos_list, l)
                right = bisect.bisect_right(pos_list, r)
                count = right - left

                if count >= threshold:
                    if count > max_freq or (count == max_freq and num < best):
                        best = num
                        max_freq = count  # Update max for this query

            result.append(best)

        return result


# Example 1
nums1 = [1,1,2,2,1,1]
queries1 = [[0,5,4],[0,3,3],[2,3,2]]
print(thresholdMajorityQueries(nums1, queries1))
#  Output: [1, -1, 2]

# Example 2
nums2 = [3,2,3,2,3,2,3]
queries2 = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]
print(thresholdMajorityQueries(nums2, queries2))
#  Output: [3, 2, 3, 2]
