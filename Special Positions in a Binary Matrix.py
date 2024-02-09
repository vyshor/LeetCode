# import numpy as np

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # print(np.matrix(mat))

        rows = {}
        cols = {}

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    if i not in rows and j not in cols:
                        count += 1
                        rows[i] = (i, j)
                        cols[j] = (i, j)
                        # print(i, j, count)
                    else:
                        if i in rows:
                            if rows[i] is not False:
                                count -= 1
                                _, y = rows[i]
                                cols[y] = False

                        rows[i] = False

                        if j in cols:
                            if cols[j] is not False:
                                x, _ = cols[j]
                                count -= 1
                                rows[x] = False

                        cols[j] = False
        return count

