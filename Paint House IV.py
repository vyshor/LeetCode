class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        dp = [0] * 6
        '''
        012
        021
        120
        210
        102
        201
        '''
        left, right = (n // 2)-1, n // 2
        while left >= 0:
            dp[0], dp[1], dp[2], dp[3], dp[4], dp[5] = \
            min(dp[1], dp[2], dp[5]) + cost[left][1] + cost[right][2], \
            min(dp[0], dp[3], dp[4]) + cost[right][1] + cost[left][2], \
            min(dp[0], dp[3], dp[5]) + cost[left][0] + cost[right][1], \
            min(dp[1], dp[2], dp[4])  + cost[right][0] + cost[left][1], \
            min(dp[1], dp[3], dp[5])  + cost[left][0] + cost[right][2], \
            min(dp[0], dp[2], dp[4]) + cost[right][0] + cost[left][2]

            left -= 1
            right += 1

        # print(dp)
        return min(dp)
