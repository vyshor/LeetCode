class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            dp[i] = min([dp[i-c]+1 if i-c >= 0 else MAX for c in coins])
        return dp[amount] if dp[amount] != MAX else -1

# Time: O(amount*n)
# Space: O(amount)

# Runtime: 1048 ms, faster than 89.69% of Python3 online submissions for Coin Change.
# Memory Usage: 14.6 MB, less than 43.01% of Python3 online submissions for Coin Change.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return amount
        dp = {tuple([0] * len(coins)):amount}
        frontlines = [tuple([0] * len(coins))]

        while len(frontlines) > 0:
            new_frontlines = []
            for frontline in frontlines:
                for i, coin in enumerate(coins):
                    new_frontline = list(frontline)
                    new_frontline[i] += 1
                    new_frontline = tuple(new_frontline)
                    if new_frontline not in dp:
                        new_val = dp[frontline] - coin
                        if new_val == 0:
                            return sum(new_frontline)
                        dp[new_frontline] = new_val
                        if new_val > 0:
                            new_frontlines.append(new_frontline)
            frontlines = new_frontlines
        return -1
                        
