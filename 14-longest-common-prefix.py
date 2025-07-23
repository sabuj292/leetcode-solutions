# Method 01

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = ""
    
    for i in range(len(strs[0])):
        for word in strs[1:]:
            if i >= len(word) or word[i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]
    
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["ab", "a"]))  # Output: "fl"


# method 2

def longestCommonPrefix(strs):
    result = []
    
    if not strs:
        return ""
    
    min_len = min(len(word) for word in strs)
    
    for i in range(min_len):
        current_char = strs[0][i]
        
        for word in strs[1:]:
            if word[i] != current_char:
                return ''.join(result)
        
        result.append(current_char)
    
    return ''.join(result)

print(longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(longestCommonPrefix(["ab", "a"]))  # Output: "fl"
