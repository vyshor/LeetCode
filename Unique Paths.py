class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        dp[(0, 0)] = 1
        for x in range(0, m):
            for y in range(0, n):
                if not (x == y and x == 0):
                    dp[(x, y)] = (dp[(x - 1, y)] if dp.get((x - 1, y)) else 0) + (
                        dp[(x, y - 1)] if dp.get((x, y - 1)) else 0)
        return dp[(m - 1, n - 1)]

# It must only move right m times
# And it must only move down n times
# And every time, it can only decide to move right or down
# After it consumes all itself action in one direction, it is only forced with other direction
# Thus, we just need to add up all the moves up to one direction is consumed max

# Runtime: 32 ms, faster than 47.94% of Python3 online submissions for Unique Paths.
# Memory Usage: 14 MB, less than 5.77% of Python3 online submissions for Unique Paths.

# Time: O(m x n)
# Space: O(m x n)