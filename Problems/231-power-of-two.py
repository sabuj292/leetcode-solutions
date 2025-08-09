from math import log2

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = log2(n)
        return x % 1 == 0