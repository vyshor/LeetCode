class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        q = []
        for i, r in enumerate(ranges):
            if r == 0:
                continue

            lower = i - r
            lower = max(lower, 0)

            upper = i + r

            q.append((lower, -upper))

        heapq.heapify(q)

        min_taps = 0
        filled = 0
        while q:
            # print(q, filled)
            lower, upper = heapq.heappop(q)
            if -upper <= filled:
                continue

            if lower < filled:
                heapq.heappush(q, (filled, upper))
                continue

            if lower > filled:
                return -1

            filled = -upper
            min_taps += 1

            if filled >= n:
                break

        if filled >= n:
            return min_taps

        return -1
