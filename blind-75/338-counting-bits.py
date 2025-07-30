class Solution(object):
    def countBits(self, n):
        result = []
        for num in range(0, n + 1):
            num = bin(num)[2:].zfill(32)
            count_1 = num.count('1')
            result.append(count_1)
        return result