class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        length = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                num = int(matrix[i - 1][j - 1])
                if num:
                    length = 1

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + num

        if length == 0:
            return 0

        max_area = 1
        possible_length = length + 1
        expected_area = possible_length * possible_length
        for i in range(2, n + 1):
            for j in range(2, m + 1):
                top_i = i - possible_length
                left_j = j - possible_length

                if top_i < 0 or left_j < 0:
                    continue

                grid_sum = dp[i][j] - dp[top_i][j] - dp[i][left_j] + dp[top_i][left_j]
                if grid_sum == expected_area:
                    length = possible_length
                    possible_length += 1
                    max_area = expected_area
                    expected_area = possible_length * possible_length

        return max_area
