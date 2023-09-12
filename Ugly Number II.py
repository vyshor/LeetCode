class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        visited = set()
        primes = [2, 3, 5]
        dp = [1]
        q = [(prime, prime, 1) for prime in primes]

        while len(dp) < n:
            product, prime, i = heapq.heappop(q)

            if product in visited:
                heapq.heappush(q, (prime * dp[i], prime, i + 1))
                continue

            visited.add(product)

            dp.append(product)
            heapq.heappush(q, (prime * dp[i], prime, i + 1))

        return dp[-1]




