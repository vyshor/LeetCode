class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        rows = [float('inf')] * n
        cols = [0] * m
        for i in range(n):
            for j in range(m):
                rows[i] = min(rows[i], matrix[i][j])
                cols[j] = max(cols[j], matrix[i][j])

        cols = set(cols)
        ans = set()
        for i in range(n):
            if rows[i] in cols:
                ans.add(rows[i])
        return ans
