class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1

        n -= 1
        dp = [1]
        q = [(prime, prime, 1) for i, prime in enumerate(primes)]
        visited = set()

        heapq.heapify(q)

        while n > 0:
            v, prime, i = heapq.heappop(q)

            if v in visited:
                heapq.heappush(q, (prime * dp[i], prime, i + 1))
                continue
            visited.add(v)

            dp.append(v)
            heapq.heappush(q, (prime * dp[i], prime, i + 1))

            n -= 1

        return v

# class Solution:
#     def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
#         if n == 1:
#             return 1
#
#         visited = set()
#         q = [1]
#         while q:
#             i = heapq.heappop(q)
#             if i in visited:
#                 continue
#             visited.add(i)
#
#             n -= 1
#             if n == 0:
#                 return i
#
#             for prime in primes:
#                 heapq.heappush(q, i * prime)

