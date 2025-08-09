
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n -1)) == 0
    
    
# Break down the approach

"""
1️⃣ Understanding the Problem
The question says:

An integer n is a power of two if there exists an integer x such that
n == 2^x

That means:

Valid examples: 1, 2, 4, 8, 16, 32, ...

Invalid examples: 0, 3, 5, 6, 10, -4, ...


2️⃣ What’s Special About Powers of Two?
If we write them in binary:

1   →  1       (only one bit set)
2   →  10      (only one bit set)
4   →  100     (only one bit set)
8   →  1000    (only one bit set)
16  →  10000   (only one bit set)



Key Observation:

    A power of two has exactly one 1 bit in binary.
    
3️⃣ How to Detect This Without Loops?
If we take a power of two n and subtract 1:

The binary flips all bits after that 1 to 1s.

n = 8  (1000)
n-1 = 7 (0111)


If we now AND them:
  1000   (n)
& 0111   (n-1)
  ----
  0000   → result is zero


This only happens for powers of two, because:

Non-powers of two have more than one 1 bit, so (n & (n - 1)) won’t be 0.

4️⃣ Step-by-Step Example
Example with n = 12:


n    = 12 → 1100
n-1  = 11 → 1011
n&(n-1) = 1000 (not zero) → Not a power of two



5️⃣ Final Logical Rule
A number n is a power of two if:

It’s positive (n > 0)

It has only one 1 bit → (n & (n - 1)) == 0

If you want, I can now give you a visual table for numbers 1–16 showing:

Decimal

Binary

(n-1) in binary

AND result
So you see the pattern clearly.

"""