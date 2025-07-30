from functools import cmp_to_key
        # custom comparator to sort by start time
def compare(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        return 0
            



class Solution(object):
    def canAttendMeetings(self, intervals):
        """"
        :type intervals: List[List[int]]
        :rtype: bool
        
        """

        # step 1: sort interval using custom comparator
        intervals.sort(key = cmp_to_key(compare))
        
        # step 2: check for overlaps
        
        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1][1]
            curr_start = intervals[i][0]
            
            if curr_start < prev_end:
                return False
            
        return True
    

sol = Solution()

intervals1 = [[0, 30], [5, 10], [15, 20]]
print(sol.canAttendMeetings(intervals1))  # False (overlap)

intervals2 = [[7, 10], [2, 4]]
print(sol.canAttendMeetings(intervals2))  # True (no overlap)
