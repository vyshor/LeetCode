class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(1, n):
            for j in range(m):
                cost = matrix[i - 1][j]
                if j > 0:
                    cost = min(cost, matrix[i - 1][j - 1])
                if j < m - 1:
                    cost = min(cost, matrix[i - 1][j + 1])
                matrix[i][j] += cost
        return min(matrix[-1])

