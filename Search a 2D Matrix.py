# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for row in matrix:
#             if not row:
#                 return False
#             if row[-1] < target:
#                 continue
#             else:
#                 ind = bisect_left(row, target)
#                 if ind >= 0 and ind < len(row) and row[ind] == target:
#                     return True
#                 return False
#         return False

# Runtime: 72 ms, faster than 62.58% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 15.9 MB, less than 41.78% of Python3 online submissions for Search a 2D Matrix.
# Time: O(n + m)
# Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(y1, x1, y2, x2, target):
            n = y2 - y1 + 1
            m = x2 - x1 + 1

            if n <= 2 and m <= 2:
                for i in range(n):
                    for j in range(m):
                        if matrix[y1 + i][x1 + j] == target:
                            return True
                return False
            else:
                midn = n // 2
                midm = m // 2

                search_quarters = [
                    (y1, x1, y1 + midn, x1 + midm),
                    (y1, x1 + midm, y1 + midn, x2),
                    (y1 + midn, x1, y2, x1 + midm),
                    (y1 + midn, x1 + midm, y2, x2),
                ]

                for (toplefty, toprightx, bottomrighty, bottomrightx) in search_quarters:
                    if matrix[toplefty][toprightx] <= target <= matrix[bottomrighty][bottomrightx]:
                        quartersearch = search(toplefty, toprightx, bottomrighty, bottomrightx, target)
                        if quartersearch:
                            return True

        return search(0, 0, len(matrix) - 1, len(matrix[0]) - 1, target)
