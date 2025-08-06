from bisect import bisect_left, bisect_right, insort
class Solution(object):
    def minTime(self, s, order, k):
        n = len(s)
        star = [0] * n
        ones = []
        total_substrings = n * (n + 1) // 2

        def count_invalid_substrings(positions):
            if not positions:
                return total_substrings
            positions = [-1] + positions + [n]
            invalid = 0
            for i in range(1, len(positions)):
                length = positions[i] - positions[i - 1] - 1
                if length > 0:
                    invalid += (length * (length + 1)) // 2
            return total_substrings - invalid

        for t in range(n):
            i = order[t]
            if not star[i]:
                star[i] = 1
                insort(ones, i)
            valid = count_invalid_substrings(ones)
            if valid >= k:
                return t

        return -1

print(minTimeToActivateString("abc", [1,0,2], 2))   # Output: 0
print(minTimeToActivateString("cat", [0,2,1], 6))   # Output: 2
print(minTimeToActivateString("xy", [0,1], 4))      # Output: -1
