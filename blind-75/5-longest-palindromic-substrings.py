

class Solution(object):
    def longestPalindrome(self, s):
        def expand_from_center(left, right):
            # Expand outward as long as valid and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        
        longest = ""
        for i in range(len(s)):
            # check odd-length palindrome centered at i
            odd = expand_from_center(i, i)
            # check even-length palindrome centered at i and i+ 1
            even = expand_from_center(i, i + 1)
            
            # update longest if we find a longer one
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
                
        return longest
    
    
print(Solution().longestPalindrome("a" * 1000))
print(Solution().longestPalindrome("abacdfgdcabba"))
print(Solution().longestPalindrome("forgeeksskeegfor"))
print(Solution().longestPalindrome(""))
print(Solution().longestPalindrome("abacdfgdcaba"))
print(Solution().longestPalindrome("ac"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("babad"))
    

# Break down of the problem


# Why  s[left+1:right]?
"""
After the last failed match, the pointers have moved one step too far:

    So the real palindrome is from left + 1 to right - 1

    But in Python, slicing is s[start:end) — it includes start but excludes end

So s[left+1 : right] is the correct slice!
"""
# visual example of this:

"""
s = "racecar"
center at 'e' → left=3, right=3

Expanding:
- s[3] == s[3]  ('e')
- s[2] == s[4]  ('c' == 'c')
- s[1] == s[5]  ('a' == 'a')
- s[0] == s[6]  ('r' == 'r')
- left = -1, right = 7 → stop

→ Return s[left+1:right] = s[0:7] = "racecar"

"""

"""

 Pointer            Value                          
 
left             went 1 too far left
right            went 1 too far right
s[left+1:right]   gets the exact valid substring

"""

"""

#  Odd-length palindrome:




    c
  b   b
a       a

"abcba"  ← center is the single middle letter `'c'`
So here, the center is at one character.

That’s why we do:

expand_from_center(i, i)

"""

# Even-length palindrome:

"""
  b   b
a       a

"abccba"  ← center is between the two `'c'`s

Now the center is between two characters.

That’s why we do:

expand_from_center(i, i + 1)

"""

# What are we really doing here::

"""
For every index i in the string:

We assume:

    Maybe there’s a palindrome of odd length centered at s[i]

    Maybe there’s a palindrome of even length centered between s[i] and s[i+1]

We try both.
"""