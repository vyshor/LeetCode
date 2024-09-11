class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        val = start ^ goal
        while val:
            count += val % 2
            val >>= 1
        return count

