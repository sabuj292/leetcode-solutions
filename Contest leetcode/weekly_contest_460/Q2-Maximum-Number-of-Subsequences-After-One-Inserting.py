class Solution:
    def numOfSubsequences(self, s):
        n = len(s)

        # Count number of T's to the right of each index
        suffix_t = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_t[i] = suffix_t[i + 1] + (1 if s[i] == 'T' else 0)

        # Count number of L's to the left of each index
        prefix_l = [0] * (n + 1)
        for i in range(n):
            prefix_l[i + 1] = prefix_l[i] + (1 if s[i] == 'L' else 0)

        # Base count of LCT
        count_l = 0
        count_lc = 0
        count_lct = 0
        for ch in s:
            if ch == 'L':
                count_l += 1
            elif ch == 'C':
                count_lc += count_l
            elif ch == 'T':
                count_lct += count_lc

        max_lct = count_lct

        # Try inserting 'L' at best place → gain = (# of C-T pairs after it)
        c_seen = 0
        ct_pairs = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'T':
                continue
            elif s[i] == 'C':
                c_seen += 1
                ct_pairs += suffix_t[i]
        max_lct = max(max_lct, count_lct + ct_pairs)

        # Try inserting 'C' at best place → gain = (# of L before × # of T after)
        for i in range(n + 1):
            left_l = prefix_l[i]
            right_t = suffix_t[i]
            gain = left_l * right_t
            max_lct = max(max_lct, count_lct + gain)

        # Try inserting 'T' at best place → gain = (# of L-C pairs before)
        l_seen = 0
        lc_pairs = 0
        for i in range(n):
            if s[i] == 'L':
                l_seen += 1
            elif s[i] == 'C':
                lc_pairs += l_seen
        max_lct = max(max_lct, count_lct + lc_pairs)

        return max_lct


sol = Solution()
print(sol.numOfSubsequences("CT"))     # ✅ Output: 1 (insert 'L' at beginning)
print(sol.numOfSubsequences("L"))      # ✅ Output: 0
print(sol.numOfSubsequences("LMCT"))   # ✅ Output: 2
print(sol.numOfSubsequences("LCCT"))   # ✅ Output: 4
print(sol.numOfSubsequences("T"))      # ✅ Output: 0
