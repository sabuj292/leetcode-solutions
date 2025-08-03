class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                prev_row = result[-1]
                new_row = [1]
                for j in range(1, i):
                    new_row.append(prev_row[j - 1] + prev_row[j])
                new_row.append(1)
                result.append(new_row)
        return result
            
# breakdown of the problem:
    # Each row starts and ends with 1. Everything in between is just the sum of the two elements diagonally above it.
    # For positions j from 1 to i - 1, add
        # prev_row[j - 1] + prev_row[j]

sol = Solution()
print(sol.generate(10))