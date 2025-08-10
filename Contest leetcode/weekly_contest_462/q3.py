import heapq
from collections import defaultdict

class Solution(object):
    def maxTotal(self, value, limit):
        buckets = defaultdict(list)
        limits_present = set()
        for v, L in zip(value, limit):
            heapq.heappush(buckets[L], -v)
            limits_present.add(L)

        live_limits = list(limits_present)
        heapq.heapify(live_limits)
        survivors = []

        def purge_buckets(thresh):
            while live_limits and live_limits[0] <= thresh:
                L = heapq.heappop(live_limits)
                buckets[L] = []

        total = 0
        while True:
            purge_buckets(len(survivors))
            while live_limits and not buckets[live_limits[0]]:
                heapq.heappop(live_limits)
            if not live_limits:
                break

            L = live_limits[0]
            v = -heapq.heappop(buckets[L])
            total += v

            heapq.heappush(survivors, L)
            x = len(survivors)

            purge_buckets(x)
            while survivors and survivors[0] <= x:
                heapq.heappop(survivors)

        return total
