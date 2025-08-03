def is_subsequence(pattern, source):
    i = 0
    for ch in source:
        if i < len(pattern) and ch == pattern[i]:
            i += 1
    return i == len(pattern)
 
print(is_subsequence("aba", "abbaa"))
print(is_subsequence("aaa", "aa")) 