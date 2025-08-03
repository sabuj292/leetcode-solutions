def findGCD(nums):

    a = min(nums)
    b = max(nums)

    gcd = max([i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0])

    return gcd

print(findGCD([7,5, 6, 8, 3]))