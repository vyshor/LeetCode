class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def pickBest(start, end):
            if (start, end) in dp:
                return dp[(start, end)]

            if start == end:
                dp[(start, end)] = piles[start]
                return dp[(start, end)]

            dp[(start, end)] = max(piles[start] - pickBest(start + 1, end), piles[end] - pickBest(start, end - 1))
            return dp[(start, end)]

        return pickBest(0, len(piles) - 1) > 0
