class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[-1][-1]:
            return 0

        dp = [[2 * n] * n for _ in range(n)]

        q = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((0, i, j))

        while q:
            dist, i, j = q.popleft()
            if dp[i][j] != 2 * n:
                continue

            dp[i][j] = dist
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < n and dp[x][y] == 2 * n:
                    q.append((dist + 1, x, y))
        # print(dp)
        path = [(-dp[0][0], 0, 0)]
        walked = set()
        while path:
            # print(path)
            dist, i, j = heapq.heappop(path)

            if (i, j) in walked:
                continue

            if i == n - 1 and j == n - 1:
                return -dist

            walked.add((i, j))
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in walked:
                    heapq.heappush(path, (max(dist, -dp[x][y]), x, y))

# class Solution:
#     def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#
#         q = deque()
#         visited = set()
#
#         safe = [[-1] * m for _ in range(n)]
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]:
#                     q.append((i, j, 0))
#                     visited.add((i, j))
#
#         while q:
#             i, j, val = q.popleft()
#             if safe[i][j] != -1:
#                 continue
#
#             safe[i][j] = val
#
#             for x,y in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
#                 if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
#                     visited.add((x,y))
#                     q.append((x, y, val+1))
#
#
#         visited = {(0, 0)}
#         q = [(-safe[0][0], 0, 0)]
#
#         # print(safe)
#
#         while q:
#             val, i, j = heapq.heappop(q)
#
#             if i == m-1 and j == n-1:
#                 return -val
#
#             for x,y in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
#                 if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
#                     visited.add((x,y))
#                     heapq.heappush(q, (max(val, -safe[x][y]), x, y))

