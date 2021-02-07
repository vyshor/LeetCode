class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        nx = len(grid)
        ny = len(grid[0])
        connected = 0

        def explore(i, j):
            if i < 0 or j < 0 or i >= nx or j >= ny or grid[i][j] == 'X':
                return False
            if grid[i][j] == '1':
                grid[i][j] = 'X'
                explore(i, j + 1)
                explore(i + 1, j)
                explore(i, j - 1)
                explore(i - 1, j)
                return True
            elif grid[i][j] == '0':
                grid[i][j] = 'X'
                return False

        for i in range(nx):
            for j in range(ny):
                if explore(i, j):
                    connected += 1

        return connected

# Time: O(n*m)
# Space: O(n*m)
# Runtime: 168 ms, faster than 42.13% of Python3 online submissions for Number of Islands.
# Memory Usage: 15.1 MB, less than 9.40% of Python3 online submissions for Number of Islands.
