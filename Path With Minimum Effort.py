import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        visited = set((0, 0))
        q = [(0, (0, 0))]
        param_x = len(heights) - 1
        param_y = len(heights[0]) - 1
        target = (param_x, param_y)
        while len(q):
            required_effort, (x, y) = heapq.heappop(q)
            if (x, y) == target:
                return required_effort
            elif (x,y) not in visited:
                visited.add((x,y))
                nxt_move = [ (x+1,y), (x-1, y), (x, y+1), (x, y-1) ]
                for move in nxt_move:
                    if param_x >= move[0] >= 0 and param_y >= move[1] >= 0 and move not in visited:
                        heapq.heappush(q, (max(required_effort, abs(heights[x][y] - heights[move[0]][move[1]])), move))


# Runtime: 856 ms, faster than 53.81% of Python3 online submissions for Path With Minimum Effort.
# Memory Usage: 16.8 MB, less than 25.49% of Python3 online submissions for Path With Minimum Effort.

# Time: O(nmlg(nm)
# Space: O(nm)