class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if not row:
                return False
            if row[-1] < target:
                continue
            else:
                ind = bisect_left(row, target)
                if ind >= 0 and ind < len(row) and row[ind] == target:
                    return True
                return False
        return False

# Runtime: 72 ms, faster than 62.58% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 15.9 MB, less than 41.78% of Python3 online submissions for Search a 2D Matrix.
# Time: O(n + m)
# Space: O(1)