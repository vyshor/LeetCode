class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(i, j):
            print("I J", i, j)
            nonlocal grid
            nums = {1, 2, 3, 4, 6, 7, 8, 9}
            for (dx, dy, dx2, dy2) in [(-1, -1, 1, 1), (0, -1, 0, 1), (-1, 0, 1, 0), (1, -1, -1, 1)]:
                i1, j1 = i + dx, j + dy
                i2, j2 = i + dx2, j + dy2
                if grid[i1][j1] + grid[i2][j2] == 10:
                    if grid[i1][j1] not in nums or grid[i2][j2] not in nums:
                        return 0

                    nums.remove(grid[i1][j1])
                    nums.remove(grid[i2][j2])
                else:
                    return 0
            return 1

        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 5:
                    count += check(i, j)
                    print("Count", count)
        return count
