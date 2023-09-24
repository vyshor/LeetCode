class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    count += grid[i][j] * 4 + 2
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= x < m and 0 <= y < n:
                            count -= min(grid[x][y], grid[i][j])

        return count


# class Solution:
#     def surfaceArea(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         total_count = 0
#
#         bottom = 0
#         count_bottom = True
#
#         next_level = True
#         while next_level:
#             next_level = False
#             new_grid = [[0] * n for _ in range(m)]
#
#             for i in range(m):
#                 for j in range(n):
#                     if grid[i][j]:
#                         if count_bottom:
#                             bottom += 1
#
#                         next_level = True
#                         for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
#                             if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
#                                 total_count += 1
#                         new_grid[i][j] = grid[i][j] - 1
#
#             if count_bottom:
#                 total_count += bottom * 2
#                 count_bottom = False
#
#             grid = new_grid
#
#         return total_count

