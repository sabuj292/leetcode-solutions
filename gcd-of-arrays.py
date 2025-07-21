
def gcd_two_num(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def findGCD(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = gcd_two_num(result, nums[i])

    return result

print(findGCD([7,5,6,8,3]))
print(findGCD([120, 300, 180, 60]))
print(findGCD([2,5,6,9,10]))