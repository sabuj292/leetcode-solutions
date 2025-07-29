class Solution(object):
    def reverseBits(self, n):
        binary = bin(n)[2:].zfill(32)
        reversed_binary = binary[::-1]
        result = int(reversed_binary, 2)
        return result
    
    
    # why bin(n)[2:]
    # bin(5)  → '0b101'

    # to remove the leading 0b we need indexing from 2
    
    # to treat every number as a 32-bit unsigned integers 
    # we need to pad the binary string with leading zeros until exactly 32 bits long
    
    # by default it gives 26 digits
    # bin(5)[2:].zfill(32)  → '00000000000000000000000000000101'

# using bitwise Solution

class Solution(object):
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # Shift result left, add last bit of n
            n >>= 1                          # Shift n right to get next bit
        return result
