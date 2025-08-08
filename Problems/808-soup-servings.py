
import math

def soupServings(n: int) -> float:
    if n >= 5000:
        return 1.0
    
    
    n = math.ceil(n / 25)
    memo = {}
    
    def dp (a, b):
        if a <= 0 and b <= 0: # both empty at same time
            return 0.5
        if a <= 0:              # A empty before B
            return 1.0
        if b <= 0:              # B empty before A
            return 0.0
        if (a, b) in memo:
            return memo[(a, b)]
        
        memo[(a, b)] = 0.25 * (dp(a - 4, b) +
                                dp(a - 3, b - 1) +
                                dp(a - 2, b- 2) +
                                dp(a - 1, b - 3)
                                )
        
        return memo[(a, b)]
    
    return dp(n, n)

# Problem Objective:
"""
What is the probability that Soup A gets empty before Soup B?
(Or they get empty at the same time, in which case we count half.)

So we're calculating :
P(A gets empty first) + 0.5 * P(A and B empty at the same time)

"""

# memo[(a, b)] or dp(a, b)= probability of success if soup A has a units and soup B has b units


# Here "memo = {}" -- is a dictionary
# In dictionary we access a value like this:
    # memo[key] --> get value stored at 'key'
    # Physical meaning:
        # Looking in the dictionary for the value at the key (a, b)
        
"""
 Why square brackets around (a, b)?
In Python:

    Square brackets [] are used to access values from a dictionary or list

    Parentheses () are used to create a tuple
"""



# Why if n >= 5000:
        # return 1.0

"""
💻 Why we use this line in code?
To avoid unnecessary recursion when n is huge.

Recursion is slow and can hit stack limits or time out.

So we say:

“If n is already very big (≥ 5000), just return 1.0 and skip the rest.”
"""

"""
🔁 Without it?
If we removed that line:

For n = 10000, the recursion would go crazy deep

Your code might crash or time out

And the answer would still be ~1.0
"""

"""
🧮 Mathematically Speaking
As n → ∞, the actual answer approaches 1.

From simulation and observations:

n = 4800 → ~0.99999

n = 5000 → already ≥ 0.999999

Difference is so small, it doesn't affect the answer
"""