import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        prime = [1] * (n-1)
        prime[0] = 0
        for i in range(2, int(math.sqrt(n))+1):
            if i-1:
                multiplier = i*i
                while multiplier < n:
                    prime[multiplier - 1] = 0
                    multiplier += i
        return sum(prime)

# Time: O(lglgn)
# Space: O(n)

# Runtime: 6424 ms, faster than 5.01% of Python3 online submissions for Count Primes.
# Memory Usage: 53 MB, less than 29.87% of Python3 online submissions for Count Primes.
