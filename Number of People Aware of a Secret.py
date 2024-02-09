class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}

        def gossip(daysLeft):
            nonlocal dp

            if daysLeft <= delay:
                return 1

            if daysLeft in dp:
                return dp[daysLeft]

            known = 1
            for i in range(delay, min(daysLeft, forget)):
                known += gossip(daysLeft - i)

            if daysLeft > forget:
                known -= 1

            dp[daysLeft] = known % MOD
            return dp[daysLeft]

        ans = gossip(n)
        # print(dp)
        return ans % MOD

# Born <- Delay -><- Spread -> Forget
# Delay = 2, Forget = 4
# Born < Delay - 0 1 > < Spread - 3 4 > Removed
#
# If person born on or before n-4, will be all removed
