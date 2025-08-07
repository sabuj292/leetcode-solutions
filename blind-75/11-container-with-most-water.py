#  Brute Force (not efficient)

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
        
#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 area = min(height[i], height[j]) * (j - i)
#                 max_area = max(max_area, area)

#         return max_area

# the above logic is correct but for large input it is very slow and will get TLE
# not efficient


# Two pointer Approach

def maxArea(self, height: List[int]) -> int:
    max_area = 0
    right = len(height) - 1
    left = 0
    
    while left < right:
        h = min(height[left], height[right])
        width = right - left
        max_area = max(max_area, h * width)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Solution Break Down

"""
Here's a clear 5-sentence summary about the pointer logic:

    The area is determined by the shorter of the two lines times the distance between them.

    To potentially increase the area, we must either increase height or maintain width.

    Since the width always shrinks when moving pointers inward, our only hope is to find a taller line.

    So we always move the pointer pointing to the shorter line, hoping the next line is taller.

    Moving the taller line doesn’t help because the shorter one still limits the water height.

"""

"""
Putting it together::
    Every time ask:
        Who the hell is the weak wall? Who is letting the water spill???
    
            Move that wall inward. Why??
                It can possibly improve height
                And even  though width gets smaller, if height improves ----> Total area can increase
"""


"""
    Key Mental Model::
        We're shrinking the container from both sides,
        but only replacing the weaker wall, hoping for a taller one.

"""