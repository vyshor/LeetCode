class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        binary = n
        while n > 0:
            n >>= 1
            binary ^= n
        return binary
