class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if i == j:
                    if grid[i][j] == 0:
                        return False
                elif i == m-j-1:
                    if grid[i][j] == 0:
                        return False
                elif grid[i][j] != 0:
                    return False
        return True
