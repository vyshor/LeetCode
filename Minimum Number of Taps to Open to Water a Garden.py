class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [i for i in range(n + 1)]

        for i, r in enumerate(ranges):
            lower = i - r
            lower = max(lower, 0)
            upper = i + r
            upper = min(upper, n)
            dp[lower] = max(dp[lower], dp[upper])

        count = 0
        end, next_end = 0, 0
        for i in range(n + 1):
            if i > next_end:
                return -1

            if i > end:
                end = next_end
                count += 1

            next_end = max(next_end, dp[i])

        return count

# class Solution:
#     def minTaps(self, n: int, ranges: List[int]) -> int:
#         q = []
#         for i, r in enumerate(ranges):
#             if r == 0:
#                 continue
#
#             lower = i - r
#             lower = max(lower, 0)
#
#             upper = i + r
#
#             q.append((lower, -upper))
#
#         heapq.heapify(q)
#
#         min_taps = 0
#         filled = 0
#         while q:
#             # print(q, filled)
#             lower, upper = heapq.heappop(q)
#             if -upper <= filled:
#                 continue
#
#             if lower < filled:
#                 heapq.heappush(q, (filled, upper))
#                 continue
#
#             if lower > filled:
#                 return -1
#
#             filled = -upper
#             min_taps += 1
#
#             if filled >= n:
#                 break
#
#         if filled >= n:
#             return min_taps
#
#         return -1
