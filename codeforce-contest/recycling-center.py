def min_coins_to_destroy_all_bags(t, test_cases):
    results = []
    for case in test_cases:
        n, c, weights = case
        weights.sort()
        ans = n
        for i in range(n + 1):
            # i = number of bags we are willing to pay for (from heaviest ones)
            cnt = i
            temp = weights[:n - i]
            temp.sort(reverse=True)  # try to destroy heavy ones earlier
            multiplier = 1
            ok = True
            for w in temp:
                if w * multiplier > c:
                    ok = False
                    break
                multiplier *= 2
            if ok:
                ans = min(ans, cnt)
        results.append(ans)
    return results


# Sample input as parsed
t = 4
test_cases = [
    (5, 10, [10, 4, 15, 1, 8]),
    (3, 42, [1000000000, 1000000000, 1000000000]),
    (10, 30, [29, 25, 2, 12, 15, 42, 14, 6, 16, 9]),
    (10, 10000000, [1, 1, 1, 1, 1, 1, 1, 1, 1, 864026633])
]

results = min_coins_to_destroy_all_bags(t, test_cases)
for res in results:
    print(res)
