def wordBreak(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
            
    return dp[n]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

print(wordBreak(s, wordDict))


#  need to recap the logic later
# need attention