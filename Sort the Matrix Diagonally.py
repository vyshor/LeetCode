class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        if n:
            m = len(mat[0])
        else:
            return mat

        def extractDiag(x, y):
            ls = []
            while x < n and y < m:
                ls.append(mat[x][y])
                x += 1
                y += 1
            return ls

        def setDiag(x, y, ls):
            i = 0
            while x < n and y < m:
                mat[x][y] = ls[i]
                i += 1
                x += 1
                y += 1

        for i in range(n):
            ll = extractDiag(i, 0)
            ll.sort()
            setDiag(i, 0, ll)
        for i in range(1, m):
            ll = extractDiag(0, i)
            ll.sort()
            setDiag(0, i, ll)

        return mat

# Runtime: 80 ms, faster than 89.70% of Python3 online submissions for Sort the Matrix Diagonally.
# Memory Usage: 14.5 MB, less than 73.91% of Python3 online submissions for Sort the Matrix Diagonally.

# Time: O(nm(lgm + lgn))
# Space: O(n+m)