class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0: 1, 1: 1, 2: 2}
        def recur(r):
            if r in dp:
                return dp[r]

            # Choose mid value
            summ = 0
            for i in range(r):
                summ += recur(i) * recur(r-1-i)
            dp[r] = summ
            return summ
        return recur(n)
