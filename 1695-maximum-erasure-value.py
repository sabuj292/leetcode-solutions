def maximumUniqueSubarray(nums):
    seen = set()
    left = 0
    current_sum = 0
    max_score = 0

    for right in range(len(nums)):
        # if duplicate found, move left pointer until it's removed
        while nums[right] in seen:
            seen.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        # add new unique element
        seen.add(nums[right])
        current_sum += nums[right]
        max_score = max(max_score, current_sum)

    return max_score

print(maximumUniqueSubarray([1, 2, 3, 2, 1, 4, 5]))