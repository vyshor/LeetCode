class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parent = {(i, j): (i, j) for i in range(row) for j in range(col)}
        on_left = set()
        on_right = set()
        water = set()

        def find(i, j):
            if parent[(i, j)] == (i, j):
                return (i, j)
            else:
                x, y = parent[(i, j)]
                original_parent = find(x, y)
                parent[(i, j)] = original_parent
                return original_parent

        def union(i1, j1, i2, j2):
            parent_1 = find(i1, j1)
            parent_2 = find(i2, j2)
            parent[parent_2] = parent_1

            if parent_2 in on_left:
                on_left.add(parent_1)
            if parent_2 in on_right:
                on_right.add(parent_1)

        for day, (i, j) in enumerate(cells):
            i -= 1
            j -= 1

            if j == 0:
                on_left.add((i, j))
            elif j == col - 1:
                on_right.add((i, j))
            water.add((i, j))

            for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1),
                           (i + 1, j - 1), (i - 1, j + 1)]:
                if (x, y) in water:
                    union(i, j, x, y)

            cur_parent = find(i, j)
            if cur_parent in on_left and cur_parent in on_right:
                return day

        return -1
