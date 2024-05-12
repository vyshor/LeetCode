class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        new_grid = [[0] * (n-2) for _ in range(n-2)]
        for i in range(n):
            for j in range(n):
                for i2 in range(i-1, i+2):
                    for j2 in range(j-1, j+2):
                        if 1 <= i2 < n-1 and 1 <= j2 < n-1:
                            new_grid[i2-1][j2-1] = max(new_grid[i2-1][j2-1], grid[i][j])
        return new_grid
