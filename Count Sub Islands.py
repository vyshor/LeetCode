class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])
        visited = set()
        islands = 0

        q = []
        for i in range(n):
            for j in range(m):
                if (i, j) in visited or grid2[i][j] == 0:
                    continue

                q = [(i, j)]
                is_island = True
                while q:
                    x, y = q.pop()
                    if (x, y) in visited:
                        continue

                    visited.add((x, y))
                    if not grid1[x][y]:
                        is_island = False

                    for (x2, y2) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if x2 >= n or x2 < 0 or y2 >= m or y2 < 0 or grid2[x2][y2] == 0:
                            continue
                        q.append((x2, y2))
                if is_island:
                    islands += 1
        return islands
