class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = []
        result = set()
        if not s:
            return 0
        count = 0
        for ch in s:
            if ch not in slist:
                slist.append(ch)
                count += 1
            else:
                result.add(count)
                slist = []
                slist.append(ch)
                count = 1
        result.add(count)

        return max(result)

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("dvdf"))