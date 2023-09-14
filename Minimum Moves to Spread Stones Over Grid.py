class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = 3
        ans = float('inf')

        stones = []
        empty = set()

        def assign(path, stones, empty_set):
            nonlocal ans

            i, j = stones.pop()
            for (x, y) in list(empty_set):
                empty_set.remove((x, y))

                if len(stones) == 0:
                    ans = min(ans, path + abs(i - x) + abs(j - y))
                else:
                    assign(path + abs(i - x) + abs(j - y), stones, empty_set)

                empty_set.add((x, y))
            stones.append((i, j))

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 1:
                    for k in range(1, grid[i][j]):
                        stones.append((i, j))
                elif grid[i][j] == 0:
                    empty.add((i, j))

        if not empty:
            return 0

        assign(0, stones, empty)
        return ans
