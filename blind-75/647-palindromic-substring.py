# def countSubstrings(s):
#     count = 0
    
#     for center in range(len(s)):
#         # odd-length palindroms
#         l, r = center, center
        
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             count += 1
#             l -= 1
#             r += 1
            
#         # Even length palindroms
#         l, r = center, center + 1
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             count += 1
#             l -= 1
#             r -= 1
            
#         return count
    
# #  Test Cases
# test_cases = [
#     "a",         # only 1 character → 1 palindrome
#     "aa",        # "a", "a", "aa" → 3
#     "aba",       # "a", "b", "a", "aba" → 4
#     "abc",       # "a", "b", "c" → 3
#     "aaa",       # "a", "a", "a", "aa", "aa", "aaa" → 6
#     "abba",      # "a", "b", "b", "a", "bb", "abba" → 6
#     "racecar",   # full palindrome + sub-parts → 10
#     "abcd",      # All different → 4
#     "aabaa"      # Try yourself: how many? → 9
# ]

# # 🖨 Print test results
# for s in test_cases:
#     result = countSubstrings(s)
#     print(f"Input: '{s}' Palindromic Substrings: {result}")


def countSubstrings(s):
    count = 0
    n = len(s)
    
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
