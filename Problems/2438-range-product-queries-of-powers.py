class Solution:
    def productQueries(self, n: int, queries: list[list[int]] -> list[int]):
        
        MOD = 1_000_000_007
        
        # as we return each answer modulo 10^9 + 7
        # and the underscore make the number readable
        
        exps= []
        # will hold the bit positions (exponents) where n has 1 bit
        # Example: if n = 15 (1111₂), then exps = [0, 1, 2, 3].
        
        i = 0
        # current bit index we're checking (LSB=0)
        x = n
        while x:
            if x & 1:
                # check the lowest bit if it's 1, then 2^i is part of the minimal powers array
                exps.append(i)
                x >>= 1
                # shift right by 1 bit to move to next bit
                i += 1
            
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)
            
        
        ans = []
        for l, r in queries:
            s = pref[r + 1] - pref[1]
            ans.append(pow(2, s, MOD))
            
        return ans            