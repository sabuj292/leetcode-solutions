# Problem Statement
# You're given an array of meeting time intervals [[start1, end1], [start2, end2], ...].
# Your goal is to determine if a person can attend all meetings (i.e., no meetings overlap).

# steps for deal the problem
# 1. Sort intervals by start Time
# 2. Check for overlap (start > end)
# 3. return False if overlap
# 4. Return True if no conflicts

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # lambda x: x[0]
        #  it's saying:

        # "Hey, give me a pair like [start, end] — I’ll return the start."
        # “For each item x in the list, use x[0] (the start) as the sorting key.”
        
        # This function is same as below function:
        
        # def get_start(interval):
            # return interval[0]
        # intervals.sort(key=get_start)

        
        # step 2: check for any overlap
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            prev_end = intervals[i - 1][1]
            if curr_start < prev_end:
                return False    # Overlap found
        return True
    
sol = Solution()

intervals1 = [[0, 30], [5, 10], [15, 20]]
print(sol.canAttendMeetings(intervals1))  # False (overlap)

intervals2 = [[7, 10], [2, 4]]
print(sol.canAttendMeetings(intervals2))  # True (no overlap)

intervals = [[i, i+1] for i in range(0, 100000, 2)]
# Expected: True (no overlap)
print(sol.canAttendMeetings(intervals))


intervals = [[0, 5]]


# Expected: True (no overlap)
print(sol.canAttendMeetings(intervals))



intervals = [[1, 5], [1, 5]]
# Expected: False (perfect overlap)
print(sol.canAttendMeetings(intervals))


intervals = [[1, 5], [5, 10]]
# Expected: True (no overlap, just touching)
print(sol.canAttendMeetings(intervals))


intervals = [[1, 10], [2, 5]]
# Expected: False (overlap)
print(sol.canAttendMeetings(intervals))


intervals = [[1, 4], [2, 5], [3, 6], [5, 7]]
# Expected: False (all overlap)

print(sol.canAttendMeetings(intervals))


intervals = [[1, 100000]] * 1000
# Expected: False (all meetings overlap at same time)

print(sol.canAttendMeetings(intervals))

