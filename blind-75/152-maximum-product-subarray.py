def maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        cur = nums[i]
        temp_max = max_prod # Save before overwriting
        
        max_prod = max(cur, cur * max_prod, cur * min_prod)
        min_prod = min(cur, cur * temp_max, cur * min_prod)
        
        result = max(result, max_prod)
        
    return result


# Efficient Solution

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reversed = nums[::-1]

        for i in range(1, len(nums)):
            if nums[i-1] != 0:
                nums[i] *= nums[i-1]
            
            if nums_reversed[i-1] != 0:
                nums_reversed[i] *= nums_reversed[i-1]
        
        return max(nums + nums_reversed)

# Solution BreakDown:

"""
🧠 Mental Trick:
Think like this on each step:

        "If I multiply with previous max or min, will I go higher or lower than starting fresh?"

If yes — take it. If not — just start over from current number.
"""

"""
🔁 Simple Real-Life Analogy
Imagine you are playing a game where you're multiplying numbers on a path. At each step, you can:

        Keep multiplying (continue the current path)

        Start over from current number

But here's the twist:

        Negative numbers act like "trap tiles" — they flip your score.

        Zeros act like "reset buttons" — you lose your progress.

So you keep track of:

        1) The best score so far (max_prod)

        2) The worst score so far (min_prod) (because it might flip to best later)

        3) The global best (result)
"""