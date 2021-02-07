class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dp = {(k, k2): set() for k in range(3) for k2 in range(3)}
        col = {k: set() for k in range(9)}
        row = {k: set() for k in range(9)}
        for x in range(9):
            for y in range(9):
                val = board[x][y]
                if val != ".":
                    if val in row[x]:
                        return False
                    if val in col[y]:
                        return False
                    if val in dp[(x // 3, y // 3)]:
                        return False
                    row[x].add(val)
                    col[y].add(val)
                    dp[(x // 3, y // 3)].add(val)

        print(row, col, dp)
        return True

# Runtime: 148 ms, faster than 9.57% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 14.5 MB, less than 17.84% of Python3 online submissions for Valid Sudoku.
# Time: O(1)
# Space: O(1)