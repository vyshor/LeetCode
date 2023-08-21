class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        topRow, topColumn = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                topColumn = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                topRow = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if topRow:
            for j in range(n):
                matrix[0][j] = 0
        if topColumn:
            for i in range(m):
                matrix[i][0] = 0

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#
#         rows = set()
#         cols = set()
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)
#
#         for i in rows:
#             for j in range(n):
#                 matrix[i][j] = 0
#
#         for j in cols:
#             for i in range(m):
#                 matrix[i][j] = 0

