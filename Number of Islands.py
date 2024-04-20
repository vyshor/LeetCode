class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        islands = 0
        visited = set()

        parent = {}

        def find(pair):
            nonlocal parent, islands
            if pair not in parent:
                parent[pair] = pair
                islands += 1

            p = parent[pair]
            if pair == p:
                return p
            else:
                new_parent = find(p)
                parent[pair] = new_parent
                return new_parent

        def union(c, p):
            nonlocal parent, islands
            c_p = find(c)
            p_p = find(p)
            parent[c_p] = p_p
            islands -= 1

        def explore(i, j):
            current_parent = find((i, j))
            visited.add((i, j))
            nonlocal grid, m, n
            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == "1" and (x, y) not in visited and current_parent != find(
                        (x, y)):
                    union((x, y), current_parent)
                    explore(x, y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    explore(i, j)

        return islands

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         nx = len(grid)
#         ny = len(grid[0])
#         connected = 0
#
#         def explore(i, j):
#             if i < 0 or j < 0 or i >= nx or j >= ny or grid[i][j] == 'X':
#                 return False
#             if grid[i][j] == '1':
#                 grid[i][j] = 'X'
#                 explore(i, j + 1)
#                 explore(i + 1, j)
#                 explore(i, j - 1)
#                 explore(i - 1, j)
#                 return True
#             elif grid[i][j] == '0':
#                 grid[i][j] = 'X'
#                 return False
#
#         for i in range(nx):
#             for j in range(ny):
#                 if explore(i, j):
#                     connected += 1
#
#         return connected
#
# # Time: O(n*m)
# # Space: O(n*m)
# # Runtime: 168 ms, faster than 42.13% of Python3 online submissions for Number of Islands.
# # Memory Usage: 15.1 MB, less than 9.40% of Python3 online submissions for Number of Islands.
