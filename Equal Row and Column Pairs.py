class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = {}

        count = 0
        for i in range(n):
            key = str(grid[i])
            if key not in dp:
                dp[key] = 1
            else:
                dp[key] += 1

        for j in range(m):
            arr = []
            for i in range(n):
                arr.append(grid[i][j])

            key = str(arr)
            if key in dp:
                count += dp[key]

        return count

# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#
#         def compare(row, col):
#             vals = grid[row]
#             for i, val in enumerate(vals):
#                 if grid[i][col] != val:
#                     return False
#             return True
#
#         count = 0
#         for i in range(n):
#             for j in range(m):
#                 count += int(compare(i, j))
#
#         return count
