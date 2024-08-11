class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        islands = 0

        def explore(i, j):
            nonlocal grid, visited, n, m, islands
            if (i, j) in visited:
                return

            visited.add((i, j))
            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if x < 0 or x >= n or y < 0 or y >= m or not grid[x][y]:
                    continue

                if (x, y) in visited:
                    continue

                explore(x, y)

        for i in range(n):
            for j in range(m):
                if grid[i][j] and (i, j) not in visited:
                    explore(i, j)
                    islands += 1

        # print(islands)
        if islands == 0 or islands >= 2:
            return 0

        places = list(visited)
        count = len(places)
        for k, (i, j) in enumerate(places):
            visited = set()
            grid[i][j] = 0
            x, y = places[k - 1]
            explore(x, y)
            if count != len(visited) + 1:
                return 1
            grid[i][j] = 1

        return 2