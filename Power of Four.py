class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return 4**int(math.log(n, 4)) == n if n > 0 else False
