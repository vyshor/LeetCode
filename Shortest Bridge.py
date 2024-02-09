class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set()

        def exploreBfs(source):
            nonlocal visited
            q = deque([source])
            while q:
                i, j = q.popleft()
                for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < n and (x, y) not in visited and grid[x][y]:
                        visited.add((x, y))
                        q.append((x, y))

        def seekBfs(q):
            nonlocal visited
            while q:
                i, j, dist = q.popleft()
                for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                        if grid[x][y]:
                            return dist

                        visited.add((x, y))
                        q.append((x, y, dist + 1))

        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    visited.add((i, j))
                    exploreBfs((i, j))
                    break

            if len(visited) != 0:
                break

        q = deque([(i, j, 0) for (i, j) in visited])
        return seekBfs(q)
