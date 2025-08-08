
# 🧠 What Is @lru_cache(None)?
"""
✅ It's a decorator that automatically remembers (caches) the results of a function.
In other words, it says:

“If I’ve already calculated this function with the same input before,
I don’t need to calculate it again — I’ll just reuse the saved answer.”
"""


"""
🔁 What Does “LRU” Mean?
LRU = Least Recently Used

It means:

It keeps track of the most recent function calls

If the cache gets too full, it will automatically remove the oldest result that hasn't been used recently

"""

# @lru_cache(None):
"""
Here, None means:

“Don’t limit the cache size — store everything.”

So it remembers all the results of the function it decorates.
"""

"""
🤔 Why It’s So Important in Recursion?
When recursion goes deep, it might:

Recalculate the same state again and again

Waste a lot of time

Possibly crash your code

So @lru_cache:

Stores the answer to each unique input

Returns it instantly next time
"""


"""
# Summary Table:

| Concept            | Meaning                                  |
| ------------------ | ---------------------------------------- |
| `@lru_cache(None)` | Cache all function results forever       |
| Saves time         | By reusing answers for repeated inputs   |
| Reduces recursion  | Avoids recalculating the same subproblem |
| `None`             | Means unlimited cache size               |
| Use in DP?         | YES — especially for top-down recursion! |


"""


import math
from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0  # Approaches 1 as n increases
        
        n = math.ceil(n / 25)

        @lru_cache(None)
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
        
        return dp(n, n)
