class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        visited = set()

        safe = [[-1] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    q.append((i, j, 0))
                    visited.add((i, j))

        while q:
            i, j, val = q.popleft()
            if safe[i][j] != -1:
                continue

            safe[i][j] = val

            for x,y in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
                    visited.add((x,y))
                    q.append((x, y, val+1))


        visited = {(0, 0)}
        q = [(-safe[0][0], 0, 0)]

        # print(safe)

        while q:
            val, i, j = heapq.heappop(q)

            if i == m-1 and j == n-1:
                return -val

            for x,y in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and (x,y) not in visited:
                    visited.add((x,y))
                    heapq.heappush(q, (max(val, -safe[x][y]), x, y))

