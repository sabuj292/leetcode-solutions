class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bad_and = None
        for i, x in enumerate(nums):
            if i != x:
                bad_and = i if bad_and is None else (bad_and & i)
        return 0 if bad_and is None else bad_and