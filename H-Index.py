class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        dp = [0] * (n+1)

        for citation in citations:
            dp[min(citation, n)] += 1

        if dp[n] == n:
            return n

        for i in range(n-1, -1, -1):
            dp[i] += dp[i+1]
            if dp[i] >= i:
                return i

        return 1

# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         n = len(citations)
#         citations.sort()
#
#         h = 0
#         for i in range(n - 1, -1, -1):
#             if citations[i] >= n - i:
#                 h = max(h, n - i)
#
#         return h
