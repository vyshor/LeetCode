class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            prev_occupied = 0
            for j in range(m):
                perimeter += grid[i][j] ^ prev_occupied
                prev_occupied = grid[i][j]
            perimeter += prev_occupied

        for j in range(m):
            prev_occupied = 0
            for i in range(n):
                perimeter += grid[i][j] ^ prev_occupied
                prev_occupied = grid[i][j]
            perimeter += prev_occupied
        return perimeter

# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         visited = set()
#         perimeter = 0
#         n = len(grid)
#         m = len(grid[0])
#         q = []
#
#         to_break = False
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j]:
#                     q.append((i, j))
#                     to_break = True
#                     break
#             if to_break:
#                 break
#
#         while q:
#             i, j = q.pop()
#             if (i, j) in visited:
#                 continue
#
#             visited.add((i, j))
#             for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
#                 if (x, y) in visited:
#                     continue
#
#                 if 0 <= x < n and 0 <= y < m and grid[x][y]:
#                     q.append((x, y))
#                 else:
#                     perimeter += 1
#         return perimeter
