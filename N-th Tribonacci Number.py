class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return [0, 1, 1][n]

        n1, n2, n3 = 0, 1, 1
        for _ in range(n - 2):
            n1, n2, n3 = n2, n3, n1 + n2 + n3
        return n3

