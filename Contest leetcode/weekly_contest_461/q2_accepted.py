class Solution(object): 
    def maxBalancedShipments(self,weight):
            n = len(weight)
            count = 0
            i = 0
        
            while i < n:
                cur_max = weight[i]
                j = i + 1
                found = False
        
                while j < n:
                    cur_max = max(cur_max, weight[j])
                    if weight[j] < cur_max:
                        count += 1
                        i = j + 1  # start next shipment after j
                        found = True
                        break
                    j += 1
        
                if not found:
                    break  # no more balanced shipment possible
            return count
        
