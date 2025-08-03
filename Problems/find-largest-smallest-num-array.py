def largest_smallest(nums):
    min_num = nums[0]
    max_num = nums[0]
    
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num


a , b = largest_smallest([2,3,9, 10])

print("largest is ", b)
print("smallest is ",a)     
    
    