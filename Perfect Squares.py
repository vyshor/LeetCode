class Solution:
    def numSquares(self, n: int) -> int:
        arr = []
        for i in range(n + 1):
            sq = i * i
            if sq == n:
                return 1
            elif sq > n:
                break
            arr.append(sq)

        dp = [float('inf')] * (n + 1)
        dp[-1] = 0
        for num in arr:
            for i in range(n, -1, -1):
                if i - num < 0:
                    break
                dp[i - num] = min(dp[i - num], dp[i] + 1)
        return dp[0]

# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [n] * (n + 1)
#         dp[-1] = 0
#
#         primes = []
#         for i in range(1, int(math.sqrt(n)) + 1):
#             primes.append(i ** 2)
#
#         for prime in primes:
#             for i in range(n, 0, -1):
#                 if prime > i:
#                     break
#                 dp[i - prime] = min(dp[i - prime], dp[i] + 1)
#
#         # print(dp)
#         return dp[0]
