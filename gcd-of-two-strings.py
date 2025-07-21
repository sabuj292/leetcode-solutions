import math
def gcdOfStrings(str1, str2):
    
    if str1 + str2 != str2 + str1:
        return ""
    
    # gcd_length = math.gcd(len(str1), len(str2))
    a = len(str1)
    b = len(str2)
    
    gcd_brute = max([i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0])

    return str1[:gcd_brute]



print(gcdOfStrings("ABCABCABC", "ABCABC"))  
print(gcdOfStrings("ABABAB", "ABAB"))       
print(gcdOfStrings("LEET", "CODE"))         
print(gcdOfStrings("AAAAA", "A"))
