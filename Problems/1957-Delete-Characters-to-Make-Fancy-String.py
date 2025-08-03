def makeFancyString(s):
    result = []
    for ch in s:
        if len(result) >= 2 and result[-1] == result[-2] == ch:
            continue
        else:
            result.append(ch)

    final_string =''.join(result)
    return final_string

# without function

def makeFancyString_manual(s):
    result = ""
    
    for ch in s:
        if len(result) >= 2 and result[-1] == result[-2] == ch:
            continue
        result += ch

    return result

# another way to solve it will better run-time
    def makeFancyString(self, s):
        result = [''] * len(s)  # Preallocate a list of empty strings
        j = 0  # Index to track valid characters in result
    
        for ch in s:
            if j >= 2 and result[j - 1] == result[j - 2] == ch:
                continue
            result[j] = ch
            j += 1
        
        return ''.join(result[:j])

print(makeFancyString("aaa"))    
print(makeFancyString_manual("aaa"))
print(makeFancyString("aaabaaa"))    
print(makeFancyString_manual("aaabaaa"))
print(makeFancyString("abcabcabc"))    
print(makeFancyString_manual("abcabcabc"))
print(makeFancyString("aaaaaaa"))    
print(makeFancyString_manual("aaaaaaa"))
print(makeFancyString(""))    
print(makeFancyString_manual(""))
print(makeFancyString("aaaaaaaaaaaaaa"))    
print(makeFancyString_manual("aaaaaaaaaaaaaa"))


