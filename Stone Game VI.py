class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        dp = [(abs(aliceValues[i]) + abs(bobValues[i]), i) for i in range(n)]
        dp.sort(reverse=True)

        netScore = 0
        for i in range(n):
            if i % 2 == 0:
                netScore += aliceValues[dp[i][1]]
            else:
                netScore -= bobValues[dp[i][1]]

        if netScore > 0:
            return 1
        elif netScore < 0:
            return -1
        return netScore
