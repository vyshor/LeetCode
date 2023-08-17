class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        maxx_score = n + m
        dp = [[maxx_score] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                    q.append((i, j))

        visited = set()
        while q:
            i, j = q.popleft()
            for (y, x) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= y < m and 0 <= x < n and (y, x) not in visited:
                    dp[y][x] = min(dp[y][x], dp[i][j] + 1)
                    q.append((y, x))
                    visited.add((y, x))
        return dp

# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         m = len(mat)
#         n = len(mat[0])
#         q = deque()
#         dp = {}
#         for i in range(m):
#             for i2 in range(n):
#                 if mat[i][i2] == 0:
#                     dp[(i, i2)] = 0
#                 else:
#                     q.append((i, i2))
#
#         q.append((-1,-1))
#         update_dp = {}
#         while len(q) > 1:
#             x, y = q.popleft()
#
#             if (x, y) == (-1, -1):
#                 dp.update(update_dp)
#                 update_dp = {}
#                 q.append((-1, -1))
#                 continue
#
#             found = False
#             smallestDistance = 999
#             for x1, y1 in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
#                 if (x1, y1) in dp:
#                     smallestDistance = min(dp[(x1, y1)]+1, smallestDistance)
#                     found = True
#             if not found:
#                 q.append((x,y))
#             else:
#                 update_dp[(x,y)] = smallestDistance
#
#
#         dp.update(update_dp)
#         for i in range(m):
#             for i2 in range(n):
#                 mat[i][i2] = dp[(i, i2)]
#         return mat

# Time: O(n x m x maxheight)
# Space: O(n x m)

# Runtime: 636 ms, faster than 76.98% of Python3 online submissions for 01 Matrix.
# Memory Usage: 17.2 MB, less than 65.64% of Python3 online submissions for 01 Matrix.
