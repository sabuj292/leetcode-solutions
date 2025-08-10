class Solution:
    def nextSpecialPalindrome(self, n: int) -> int:
        n_str = str(n)
        L_n = len(n_str)

        evens, odds = [2,4,6,8], [1,3,5,7,9]

        # ---- generate profiles bucketed by length (count[d] = d if digit used)
        def even_subsets():
            res = [[]]
            for d in evens:
                res += [r + [d] for r in res]
            return res

        profiles_by_len = {}
        subs = even_subsets()

        # even-length: any non-empty subset of even digits
        for s in subs:
            if not s: 
                continue
            length = sum(s)
            cnt = {d: d for d in s}
            profiles_by_len.setdefault(length, []).append(cnt)

        # odd-length: one odd center + any subset of evens
        for c in odds:
            for s in subs:
                length = c + sum(s)
                cnt = {d: d for d in s}
                cnt[c] = c
                profiles_by_len.setdefault(length, []).append(cnt)

        # ---- smallest palindrome from counts (no bound)
        def min_pal_from_counts(cnt):
            center = None
            for d in range(1, 10):
                if cnt.get(d, 0) % 2 == 1:
                    center = d
                    break
            left = []
            for d in range(1, 10):
                left.append(str(d) * (cnt.get(d, 0) // 2))
            left = "".join(left)
            if center is None:
                return left + left[::-1]
            return left + str(center) + left[::-1]

        # ---- smallest palindrome strictly > n_str with same length and counts
        def min_pal_gt_bound(n_str, cnt):
            L = len(n_str)
            if sum(cnt.values()) != L:
                return None

            counts = [0]*10
            for d, c in cnt.items():
                counts[d] = c

            res = [''] * L

            def can_finish_even_counts():
                # after placing center (odd length), all remaining must be even
                for d in range(10):
                    if counts[d] % 2 != 0:
                        return False
                return True

            def dfs(i, equal_prefix, already_greater):
                j = L - 1 - i
                if i > j:
                    # finished both sides; must be strictly greater
                    return already_greater

                if i < j:
                    # choose digit d for both ends
                    start = 1
                    bound_digit = int(n_str[i]) if equal_prefix and not already_greater else 0
                    for d in range(start, 10):
                        if counts[d] >= 2:
                            if not already_greater and equal_prefix and d < bound_digit:
                                continue
                            # place
                            counts[d] -= 2
                            res[i] = res[j] = str(d)
                            next_equal = equal_prefix and (d == bound_digit) and not already_greater
                            next_greater = already_greater or (equal_prefix and d > bound_digit)
                            if dfs(i+1, next_equal, next_greater):
                                return True
                            counts[d] += 2
                    return False
                else:
                    # center position
                    bound_digit = int(n_str[i]) if equal_prefix and not already_greater else 0
                    for d in range(1, 10):
                        if counts[d] >= 1:
                            # center choice must leave the rest even
                            counts[d] -= 1
                            ok_even = can_finish_even_counts()
                            if ok_even:
                                if not already_greater and equal_prefix and d < bound_digit:
                                    counts[d] += 1
                                    continue
                                res[i] = str(d)
                                next_greater = already_greater or (equal_prefix and d > bound_digit)
                                # at the end, we must be strictly greater
                                if next_greater:
                                    return True
                            counts[d] += 1
                    return False

            if dfs(0, True, False):
                return "".join(res)
            return None

        # 1) try same length
        if L_n in profiles_by_len:
            best = None
            for cnt in profiles_by_len[L_n]:
                cand = min_pal_gt_bound(n_str, cnt)
                if cand is not None and (best is None or int(cand) < int(best)):
                    best = cand
            if best is not None:
                return int(best)

        # 2) try longer lengths—first available length gives the answer
        for length in sorted([x for x in profiles_by_len if x > L_n]):
            best = None
            for cnt in profiles_by_len[length]:
                cand = min_pal_from_counts(cnt)
                if best is None or int(cand) < int(best)):
                    best = cand
            if best is not None:
                return int(best)

        return -1

print(Solution().nextSpecialPalindrome(2))    # 22
print(Solution().nextSpecialPalindrome(33))