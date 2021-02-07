class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        state = [['0'] * n for _ in range(m)]
        coord = []

        def upflow(i, j, level, ocean):
            if i < 0 or j < 0 or i >= m or j >= n or state[i][j] == ocean:
                return False
            elif matrix[i][j] >= level:
                if state[i][j] == 'P':
                    state[i][j] = 'X'
                    coord.append([i, j])
                else:
                    state[i][j] = ocean
                upflow(i - 1, j, matrix[i][j], ocean)
                upflow(i + 1, j, matrix[i][j], ocean)
                upflow(i, j - 1, matrix[i][j], ocean)
                upflow(i, j + 1, matrix[i][j], ocean)

        for x in range(m):
            upflow(x, 0, -1, 'P')
        for y in range(n):
            upflow(0, y, -1, 'P')

        for x in range(m):
            upflow(x, n - 1, -1, 'A')
        for y in range(n):
            upflow(m - 1, y, -1, 'A')

        return coord

# Time: O(n*m) # Only repeating visiting those that are in the answers
# Space: O(n*m)
# Runtime: 324 ms, faster than 71.47% of Python3 online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15.5 MB, less than 10.00% of Python3 online submissions for Pacific Atlantic Water Flow.