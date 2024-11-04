class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recur(m, j):
            # print(m, j)
            if j == 1:
                return 0

            x = 2 ** (m - 1)
            if j == x:
                return 1
            if j > x:
                return not recur(m - 1, 2 * x - j)

            y = j
            for i in range(1, m):
                minus = 2 ** (i - 1)
                if y - minus <= 0:
                    return recur(i, j)
                y -= minus
            return 0

        return str(int(recur(n, k)))
