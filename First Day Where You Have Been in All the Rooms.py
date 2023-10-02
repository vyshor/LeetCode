class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        dp[1] = 2

        for i in range(2, n):
            # nextVisit[i-1] is the location where it is jumped back
            # Days to reach previous step = dp[i-1]
            # Days to reach the reset position from previous step = 1
            # Days to reach back previous step from reset position = dp[i-1] - dp[nextVisit[i-1]]
            # Days to reach from previous step to next step = 1
            dp[i] = ((dp[i-1]+2) + (dp[i-1] - dp[nextVisit[i-1]]) % (10 ** 9 + 7))

        # print(dp)
        return dp[-1] % (10 ** 9 + 7)
