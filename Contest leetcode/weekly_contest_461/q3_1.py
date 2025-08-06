class Solution(object):    
    def minTime(self, s, order, k):
        n = len(s)
        total = n * (n + 1) // 2  # all substrings
        star = [0] * n

        intervals = []  # stores non-star intervals: [start, end]
        intervals.append([0, n - 1])
        invalid = total  # initially all substrings are invalid

        import bisect

        def remove_interval(i):
            return (i * (i + 1)) // 2

        for t in range(n):
            idx = order[t]
            if star[idx]:
                continue
            star[idx] = 1

            # Find the interval [l, r] where idx belongs
            pos = -1
            for i in range(len(intervals)):
                l, r = intervals[i]
                if l <= idx <= r:
                    pos = i
                    break

            if pos == -1:
                # already a star
                pass
            else:
                l, r = intervals[pos]
                invalid -= remove_interval(r - l + 1)
                intervals.pop(pos)
                if l <= idx - 1:
                    intervals.insert(pos, [l, idx - 1])
                    invalid += remove_interval(idx - l)
                    pos += 1
                if idx + 1 <= r:
                    intervals.insert(pos, [idx + 1, r])
                    invalid += remove_interval(r - idx)

            valid = total - invalid
            if valid >= k:
                return t

        return -1
