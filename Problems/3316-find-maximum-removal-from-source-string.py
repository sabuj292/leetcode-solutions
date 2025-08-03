
class Solution(object):

    def maximumRemovals(source, pattern, targetIndices):
 
        def isSubsequence(s, t):
            """Check if s is a subsequence of t"""
            i = 0  # pointer for s
            for char in t:
                if i < len(s) and s[i] == char:
                    i += 1
            return i == len(s)

        def canRemove(k):
            """Check if we can remove the first k elements from targetIndices"""
            # Create a set of indices to remove
            to_remove = set(targetIndices[:k])
            
            # Build the resulting string after removals
            remaining = []
            for i, char in enumerate(source):
                if i not in to_remove:
                    remaining.append(char)
            
            remaining_str = ''.join(remaining)
            
            # Check if remaining string is a subsequence of pattern
            return isSubsequence(remaining_str, pattern)

        # Binary search for the maximum number of removals
        left, right = 0, len(targetIndices)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            
            if canRemove(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result