class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {}

        def pickStones(i):
            if i == n:
                return 0

            if i in dp:
                return dp[i]

            best_val = float('-inf')
            prefix_sum = 0
            for j in range(i, min(i + 3, n)):
                prefix_sum += stoneValue[j]
                best_val = max(best_val, prefix_sum - pickStones(j + 1))

            dp[i] = best_val
            return dp[i]

        aliceScore = pickStones(0)
        if aliceScore > 0:
            return "Alice"
        elif aliceScore == 0:
            return "Tie"
        else:
            return "Bob"
