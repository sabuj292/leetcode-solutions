def minimum_removals_to_balance(nums, k):
    nums.sort()
    n = len(nums)
    i = 0
    max_len = 0
    
    for j in range(n):
        while nums[j] > nums[i] * k:
            i += 1
        max_len = max(max_len, j - i + 1)
    
    return n - max_len


# Test Cases
tests = [
    # Basic Test Cases
    {"nums": [2, 1, 5], "k": 2, "expected": 1},
    {"nums": [1, 6, 2, 9], "k": 3, "expected": 2},
    {"nums": [4, 6], "k": 2, "expected": 0},

    # Edge Cases
    {"nums": [100], "k": 10, "expected": 0},
    {"nums": [7, 7, 7, 7], "k": 1, "expected": 0},
    {"nums": [1, 2, 3], "k": 1, "expected": 2},
    {"nums": [9, 6, 3, 1], "k": 3, "expected": 1},

    # Tricky Sort-Aware Case
    {"nums": [5, 10, 2, 20, 1], "k": 4, "expected": 3}
]

# Run and Print Results
for idx, test in enumerate(tests, 1):
    result = minimum_removals_to_balance(test["nums"], test["k"])
    print(f"Test Case {idx}:")
    print(f"Input: nums = {test['nums']}, k = {test['k']}")
    print(f"Expected Output: {test['expected']}")
    print(f"Actual Output:   {result}")
    print(f"{' PASS' if result == test['expected'] else ' FAIL'}")
    print("-" * 40)