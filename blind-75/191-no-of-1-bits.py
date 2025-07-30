class Solution(object):
    def hammingWeight(self, n):
        binary_num = bin(n)[2:].zfill(32)
        count_ones = binary_num.count('1')
        return count_ones
    
    
sol = Solution()
print(sol.hammingWeight(0))          # 0
print(sol.hammingWeight(1))          # 1
print(sol.hammingWeight(2))          # 1
print(sol.hammingWeight(3))          # 2
print(sol.hammingWeight(5))          # 2
print(sol.hammingWeight(7))          # 3
print(sol.hammingWeight(255))        # 8
print(sol.hammingWeight(1023))       # 10
print(sol.hammingWeight(4294967295)) # 32
print(sol.hammingWeight(2147483648)) # 1



# using Bitwise Trick

n = 13
count = 0
while n:
    count += n & 1
    n >>= 1
print(count)  # Output: 3

