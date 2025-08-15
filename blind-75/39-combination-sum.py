# problem statement
"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""


def combinationSum(candidates, target):
    result = []
    
    def backtrack(start, current, total):
        
        # base case
        # if we found a valid combination, save it
        if total == target:
            result.append(list(current)) # appeding a copy of current to result
            return                           # list(current) is needed because current will change later (mutable list)
            
        
        if total > target:
            return
        # what it does:
        # if the sum so far is greater than the target
            # stop exploring this path
            # all numbers are positive, adding more will only make the sum bigger, so no chance to hit target
            
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])
            # passing i not i + 1 because reuse is allowesd
            # exploration step - try continuing with the current choice
            current.pop()
        backtrack(0, [], 0)
        # it start recursion
        return result