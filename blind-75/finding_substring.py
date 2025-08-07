
def finding_substring(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
            
    return substrings
    # for ss in substrings:
    #     if ss in wordDict:
    #         continue
        
            
s= "catsandog"
print(finding_substring(s))