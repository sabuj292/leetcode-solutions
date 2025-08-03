
class Solution(object):    
    def maxBalancedShipments(self, weights):
        n = len(weight)
        count = 0
        i = 0

        while i < n - 1:
            cur_max = weight[i]
            j = i
            found = False

            while j < n:
                cur_max = max(cur_max, weight[j])
                if weight[j] < cur_max:
                    # Valid shipment ends at j
                    count += 1
                    i = j + 1  # next shipment starts after j
                    found = True
                    break
                j += 1

            if not found:
                break

        return count


print(maxBalancedShipments([2, 5, 1, 4, 3]))  # ➞ 2
print(maxBalancedShipments([4, 4]))          # ➞ 0
print(maxBalancedShipments([1, 3, 2, 6, 4, 7, 1]))  # ➞ 3
