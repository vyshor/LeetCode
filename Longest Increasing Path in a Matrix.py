from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_x = len(matrix)
        max_y = len(matrix[0])
        dp = {}
        visited = set([])
        depth = {}

        def largerThanCheck(x,y):
            neighbours = [(1,0), (-1,0), (0,1), (0,-1)]
            next_moves = []
            for add_x, add_y in neighbours:
                new_x = x + add_x
                new_y = y + add_y
                if new_x >= max_x or new_x < 0 or new_y >= max_y  or new_y < 0:
                    continue
                else:
                    if matrix[new_x][new_y] > matrix[x][y]:
                        next_moves.append((new_x, new_y))
            dp[(x,y)] = next_moves

        for i in range(max_x):
            for i2 in range(max_y):
                largerThanCheck(i, i2)

        def resolveDepth(x,y):
            if (x,y) in depth:
                return depth[(x,y)]
            else:
                if len(dp[(x,y)]) == 0:
                    return 1
                else:
                    currentDepth = max([resolveDepth(_x, _y) for _x, _y in dp[(x,y)]])
                    depth[(x,y)] = currentDepth+1
                    return currentDepth+1

        max_depth = 1
        for k, v in dp.items():
            if len(v) > 0:
                x, y = k
                givenDepth = resolveDepth(x,y)
                if givenDepth > max_depth:
                    max_depth = givenDepth
        return max_depth

# Time: O(nm)
# Space: O(nm)

# Runtime: 640 ms, faster than 16.06% of Python3 online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 24 MB, less than 5.00% of Python3 online submissions for Longest Increasing Path in a Matrix.
