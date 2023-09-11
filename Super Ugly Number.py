class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1

        visited = set()
        q = [1]
        while q:
            i = heapq.heappop(q)
            if i in visited:
                continue
            visited.add(i)

            n -= 1
            if n == 0:
                return i

            for prime in primes:
                heapq.heappush(q, i * prime)

