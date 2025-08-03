from collections import defaultdict, deque
import math

#  not perfrom get time limit exceeded


# Utility function to check if a number is prime
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0: return False
    return True

def min_jumps(nums):
    n = len(nums)
    if n == 1:
        return 0

    # Preprocess: map values to indices where they occur
    value_to_indices = defaultdict(list)
    for idx, num in enumerate(nums):
        value_to_indices[num].append(idx)

    # Mark all prime numbers in nums
    primes_in_nums = set()
    for num in set(nums):
        if is_prime(num):
            primes_in_nums.add(num)

    # Queue for BFS: (index, steps)
    queue = deque()
    queue.append((0, 0))

    visited = [False] * n
    visited[0] = True

    used_primes = set()  # To avoid teleporting multiple times using same prime

    while queue:
        idx, steps = queue.popleft()

        # Reached end
        if idx == n - 1:
            return steps

        # Adjacent step: i + 1
        if idx + 1 < n and not visited[idx + 1]:
            visited[idx + 1] = True
            queue.append((idx + 1, steps + 1))

        # Adjacent step: i - 1
        if idx - 1 >= 0 and not visited[idx - 1]:
            visited[idx - 1] = True
            queue.append((idx - 1, steps + 1))

        #  Prime teleportation
        val = nums[idx]
        if val in primes_in_nums and val not in used_primes:
            for target_idx in range(n):
                if not visited[target_idx] and target_idx != idx and nums[target_idx] % val == 0:
                    visited[target_idx] = True
                    queue.append((target_idx, steps + 1))
            used_primes.add(val)  # mark prime as used

    return -1  # Should never happen if input is valid


print(min_jumps([1, 2, 4, 6]))        # Output: 2
print(min_jumps([2, 3, 4, 7, 9]))     # Output: 2
print(min_jumps([4, 6, 5, 8]))        # Output: 3
print(min_jumps([3, 6, 9, 12, 15]))   # Output: 1 (can teleport all the way!)
