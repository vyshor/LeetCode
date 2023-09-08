class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbours = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1),
                                 (i + 1, j - 1), (i - 1, j + 1)]:
                        if 0 <= x < m and 0 <= y < n:
                            neighbours[x][y] += 1

        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    if neighbours[i][j] < 2 or neighbours[i][j] > 3:
                        board[i][j] = 0
                else:
                    if neighbours[i][j] == 3:
                        board[i][j] = 1


