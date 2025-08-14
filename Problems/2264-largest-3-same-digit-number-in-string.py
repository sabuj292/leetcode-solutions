class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = set()
        for i in range(0, len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if num[i] == '9':
                    return '999'
                result.add(num[i])
        if not result or (len(num) < 3): 
            return ""
        return str(max(result) * 3)
    
    
 # another way 

class Solution(object):
    def largestGoodInteger(self, num):
        best = None
        for i in range(len(num) - 2):
            a = num[i]
            if a == num[i + 1] == num[i + 2]:
                if best is None or a > best:
                    best = a
                    if best == '9':
                        return '999'
        return best * 3 if best else ""