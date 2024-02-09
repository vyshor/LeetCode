class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xorr = x ^ y
        count = 0
        while xorr > 0:
            count += xorr % 2
            xorr >>= 1
        return count
