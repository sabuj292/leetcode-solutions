from collections import Counter

class Solution(object):
    def minCost(self, basket1, basket2):
        total = Counter(basket1) + Counter(basket2)

        # Check if we can make the baskets equal
        for fruit, count in total.items():
            if count % 2 != 0:
                return -1

        count1 = Counter(basket1)
        count2 = Counter(basket2)

        # Get the excess fruits in each basket
        extra1 = []
        extra2 = []

        for fruit in total:
            need = total[fruit] // 2
            if count1[fruit] > need:
                extra1.extend([fruit] * (count1[fruit] - need))
            elif count2[fruit] > need:
                extra2.extend([fruit] * (count2[fruit] - need))

        # Sort for optimal swapping
        extra1.sort()
        extra2.sort(reverse=True)

        min_value = min(total.keys())
        total_cost = 0

        for a, b in zip(extra1, extra2):
            total_cost += min(min(a, b), 2 * min_value)

        return total_cost
