class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[-1] = 0

        primes = []
        for i in range(1, int(math.sqrt(n)) + 1):
            primes.append(i ** 2)

        for prime in primes:
            for i in range(n, 0, -1):
                if prime > i:
                    break
                dp[i - prime] = min(dp[i - prime], dp[i] + 1)

        # print(dp)
        return dp[0]
