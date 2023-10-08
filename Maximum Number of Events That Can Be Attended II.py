class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        m = len(events)

        events.sort()
        dp = [0] * (k + 1)

        q = []
        i = 0
        for event in events:
            (start, end, score) = event
            while q and q[0][0] < start:
                _, j, new_score = heapq.heappop(q)
                dp[j] = max(dp[j], new_score)

            for j in range(k, 0, -1):
                heapq.heappush(q, (end, j - 1, dp[j] + score))

        while q:
            _, j, new_score = heapq.heappop(q)
            dp[j] = max(dp[j], new_score)

        return max(dp)

