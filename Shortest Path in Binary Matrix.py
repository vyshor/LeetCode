import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = [(1, (0,0))]
        visited = set((0,0))
        max_x = len(grid)
        max_y = len(grid[0])
        target = (max_x-1, max_y - 1)
        if grid[0][0]:
            return -1

        def next_move(move):
            x, y = move
            return [
                (x+1, y),
                (x, y+1),
                (x+1, y+1),
                (x-1, y),
                (x, y-1),
                (x-1, y-1),
                (x+1, y-1),
                (x-1, y+1)
            ]

        def add_next(move, dist):
            for next_m in next_move(move):
                if next_m not in visited:
                    x, y = next_m
                    if 0 <= x < max_x and 0 <= y < max_y and not grid[x][y]:
                        visited.add(next_m)
                        heapq.heappush(q, (dist+1, next_m))

        while len(q) > 0:
            dist, next_m = heapq.heappop(q)
            if next_m == target:
                return dist
            add_next(next_m, dist)
        return -1
            
    # Time:O(n^2)
    # Space: O(n^2)

    # Runtime: 696 ms, faster than 58.28% of Python3 online submissions for Shortest Path in Binary Matrix.
# Memory Usage: 15.7 MB, less than 20.88% of Python3 online submissions for Shortest Path in Binary Matrix.
