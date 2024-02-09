# import numpy as np

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe = set()

        m = len(board)
        n = len(board[0])

        q = []
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == "O":
                    q.append((i, j))

        for j in range(n):
            for i in [0, m - 1]:
                if board[i][j] == "O":
                    q.append((i, j))

        while q:
            x, y = q.pop()
            safe.add((x, y))

            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n and board[i][j] == "O" and (i, j) not in safe:
                    q.append((i, j))

        # print(safe)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"


