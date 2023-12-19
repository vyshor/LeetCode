class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n = len(img)
        m = len(img[0])
        summ = [[0] * m for _ in range(n)]
        count = [[1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                summ[i][j] += img[i][j]
                for (x, y) in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j + 1),
                               (i - 1, j + 1), (i + 1, j - 1)]:
                    if 0 <= x < n and 0 <= y < m:
                        count[x][y] += 1
                        summ[x][y] += img[i][j]

        for i in range(n):
            for j in range(m):
                img[i][j] = summ[i][j] // count[i][j]

        return img
