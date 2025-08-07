def countSubstrings(s):
    count = 0
    n = len(s)
    
    #  in the following total center = 2 * n -1
    for center in range(2 * n - 1):
        left = center // 2
        right = left + (center % 2)
        
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
    return count


test_cases = [
    "a",         # 1
    "aa",        # 3
    "aba",       # 4
    "abc",       # 3
    "aaa",       # 6
    "abba",      # 6
    "racecar",   # 10
    "abcd",      # 4
    "aabaa"      # 9
]

for s in test_cases:
    print(f"Input: '{s}' Palindromic Substrings: {countSubstrings(s)}")



# Problem Solving Approach: Expand around the center

"""
There are two kinds of centers:

    Centers on a character — for odd-length palindromes

    Centers between characters — for even-length palindromes
"""

"""
   s = "abc"
index:   0   1   2
         a   b   c
        ^   ^   ^

Possible positions:

    👉 Odd-length centers (on characters):
Center on a (index 0)

Center on b (index 1)

Center on c (index 2)

✅ Total = 3 centers

👉 Even-length centers (between characters):
Between a and b → index 0.5

Between b and c → index 1.5

✅ Total = 2 centers

    🎯 Total Centers = 3 (odd) + 2 (even) = 5
And for any string of length n, this pattern always happens:

n odd-length centers

n - 1 even-length centers


"""