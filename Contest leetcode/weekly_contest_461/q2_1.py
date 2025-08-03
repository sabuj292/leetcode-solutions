def maxBalancedShipments(weights):
    n = len(weights)
    start = 0
    count = 0

    while start < n:
        max_val = weights[start]
        end = start + 1
        found = False

        while end < n:
            max_val = max(max_val, weights[end])
            if weights[end] < max_val:
                print(f"Balanced shipment found: {weights[start:end+1]}")
                count += 1
                start = end + 1
                found = True
                break
            end += 1

        if not found:
            start += 1

    print(f"Total balanced shipments: {count}")
    return count


print("Test 1:")
maxBalancedShipments([2, 5, 1, 4, 3])

print("Test 2:")
maxBalancedShipments([4, 4])

print("Test 3:")
maxBalancedShipments([1, 3, 2, 6, 4, 7, 1])
