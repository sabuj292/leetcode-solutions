def gcd_basic(a, b):
    factors_a = [i for i in range (1, a + 1) if a % i == 0]
    factors_b = [i for i in range (1, b + 1) if b % i == 0]
    
    common = set(factors_a).intersection(factors_b)
    return max(common)

def gcd_brute_force(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

# brute force method above in just one line of code

gcd_brute = lambda a, b: max([i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0])

# Euclidean Method

def gcd_euclidean (a, b):
    while b != 0:
        a , b = b, a % b
    return a

print(gcd_basic(12, 15))
print(gcd_brute_force(15, 30))
print(gcd_brute(30, 50))
print(gcd_euclidean(30, 90))