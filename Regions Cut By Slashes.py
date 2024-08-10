class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        islands = (n * n) << 2
        parents = [i for i in range(islands)]

        def find(i):
            nonlocal parents
            if parents[i] == i:
                return i

            new_parent = find(parents[i])
            parents[i] = new_parent
            return new_parent

        def union(i, j):
            nonlocal parents, islands, n
            if i < 0 or i >= len(parents) or j < 0 or j >= len(parents):
                return

            parent_i = find(i)
            parent_j = find(j)
            if parent_i != parent_j:
                islands -= 1
                parents[parent_j] = parent_i

        def get_pos(i, j, dir):
            return ((i * n + j) << 2) + dir

        for i in range(n):
            for j, c in enumerate(grid[i]):
                pos = get_pos(i, j, 0)
                if c == "/":
                    union(pos, get_pos(i, j, 3))
                    union(pos, get_pos(i - 1, j, 2))
                    if j != 0:
                        union(pos, get_pos(i, j - 1, 1))

                    union(pos + 1, pos + 2)
                    union(pos + 2, get_pos(i + 1, j, 0))
                    if j != n - 1:
                        union(pos + 1, get_pos(i, j + 1, 3))

                elif c == "\\":
                    union(pos, pos + 1)
                    union(pos, get_pos(i - 1, j, 2))
                    if j != n - 1:
                        union(pos, get_pos(i, j + 1, 3))

                    union(pos + 2, pos + 3)
                    union(pos + 2, get_pos(i + 1, j, 0))
                    if j != 0:
                        union(pos + 3, get_pos(i, j - 1, 1))
                else:
                    union(pos, pos + 1)
                    union(pos, pos + 2)
                    union(pos, pos + 3)
                    union(pos, get_pos(i - 1, j, 2))
                    union(pos, get_pos(i + 1, j, 0))
                    if j != 0:
                        union(pos, get_pos(i, j - 1, 1))
                    if j != n - 1:
                        union(pos, get_pos(i, j + 1, 3))
                # print(parents, islands)
        # print(parents)
        return islands
