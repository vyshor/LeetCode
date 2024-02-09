class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * n
        sales = {}

        for start, end, gold in offers:
            if start == 0:
                dp[end] = max(dp[end], gold)

            else:
                start -= 1
                if start not in sales:
                    sales[start] = [(end, gold)]
                else:
                    sales[start].append((end,gold))

        for i in range(n):
            if i > 0:
                dp[i] = max(dp[i], dp[i-1])

            if i in sales:
                for end, gold in sales[i]:
                    dp[end] = max(dp[end], dp[i]+gold)

        # print(dp)
        return dp[-1]
