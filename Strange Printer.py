class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        m = [[0]*n for _ in range(n)]
        for i in range(n-1, -1 ,-1):
            m[i][i] = 1
            for j in range(i+1, n):
                m[i][j] = m[i][j-1] + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        m[i][j] = min(m[i][j], m[i][k] + (m[k+1][j-1] if k + 1 < j else 0))
        return m[0][n-1]