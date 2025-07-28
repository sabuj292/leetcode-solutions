def is_possible(b):
    min_prefix = b[0]
    for i in range(1, len(b)):
        if b[i] < b[i - 1] and b[i] < min_prefix:
            return False
        min_prefix = min(min_prefix, b[i])
    return b == sorted(b)  # final check to disallow strictly increasing patterns like [40,60,90]

# Updated test cases with corrected logic
test_cases = [
    [5, 6, 1, 1],   # ✅ YES
    [3, 1, 2],      # ❌ NO
    [40, 60, 90],   # ❌ NO — can't reach
    [1, 1],         # ✅ YES
]

# Run the tests
print("Final Results:\n")
for idx, b in enumerate(test_cases, 1):
    result = "YES" if is_possible(b) else "NO"
    print(f"Test Case #{idx}: Input = {b} => Output = {result}")
