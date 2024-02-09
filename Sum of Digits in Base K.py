class Solution:
    def sumBase(self, n: int, k: int) -> int:
        count = 0
        while n:
            count += n % k
            n //= k
        return count
