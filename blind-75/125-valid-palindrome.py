# 1st- method::


# class solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = ''
#         for char in s:
#             if char.isalnum():
#                 cleaned += char.lower()
#         return cleaned == cleaned[::-1]
    
  
  
#   char.isalnum() returns True if char is a letter (a–z or A–Z) or a digit (0–9).

# This condition filters out everything else — spaces, punctuation, symbols, etc.
  
  
    
# explaination of cleaned[::-1]

# reversed = ''
# for i in range(len(cleaned)-1, -1, -1):
# reversed += cleaned[i]



 # 2nd--->  Two Pointer Strategy
 
#  We’ll use two pointers:

# left starts from the beginning (0)

# right starts from the end (len(s) - 1)

# We’ll:

# Move left forward and right backward.

# Skip any non-alphanumeric characters.

# Compare s[left] and s[right] after converting them to lowercase.

# If they don’t match → return False.

# If they meet/cross → return True.
            
            
            
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


#  Test Cases
solution = Solution()

test_cases = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("", True),
    ("   ", True),
    ("No 'x' in Nixon", True),
    ("12321", True),
    ("123@321", True),
    ("1a2", False),
]

for i, (input_str, expected) in enumerate(test_cases, 1):
    result = solution.isPalindrome(input_str)
    print(f"Test Case {i}: Input = {repr(input_str)}")
    print(f"Expected = {expected}, Got = {result}")
    print("Passed" if result == expected else " Failed", end="\n\n")

