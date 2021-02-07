import heapq


class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        dp = {}
        first_int = matrix[0][0]
        h = [(first_int, (0, 0))]
        dp[(0, 0)] = first_int
        while len(h) > 0:
            smallest_pair = heapq.heappop(h)
            val = smallest_pair[0]
            coord = smallest_pair[1]
            if val == target:
                return True
            if val > target:
                continue
            else:
                y, x = coord
                if y < len(matrix) - 1:
                    val2 = matrix[y + 1][x]
                    val2_coord = (y + 1, x)
                    if not dp.get(val2_coord):
                        heapq.heappush(h, (val2, val2_coord))
                        dp[val2_coord] = val2
                if x < len(matrix[0]) - 1:
                    val2 = matrix[y][x + 1]
                    val2_coord = (y, x + 1)
                    if not dp.get(val2_coord):
                        heapq.heappush(h, (val2, val2_coord))
                        dp[val2_coord] = val2
        return False

# Runtime: 252 ms, faster than 5.35% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 22.4 MB, less than 5.04% of Python3 online submissions for Search a 2D Matrix II.
# Time: O(m * n)
# Space: O(m * n)

import heapq


class Solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            ind = bisect_left(row, target)
            if ind >= 0 and ind < len(row) and row[ind] == target:
                return True
        return False
