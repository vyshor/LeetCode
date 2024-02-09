class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []
        dp.append([poured])
        for i in range(1, query_row + 1):
            prev_row = dp[-1]
            new_row = []

            first = (prev_row[0] - 1) / 2
            if first < 0:
                new_row.append(0)
            else:
                new_row.append(first)

            for j in range(len(dp[-1]) - 1):
                left = (prev_row[j] - 1) / 2
                if left < 0:
                    left = 0
                right = (prev_row[j + 1] - 1) / 2
                if right < 0:
                    right = 0
                new_row.append(left + right)

            last = (prev_row[-1] - 1) / 2
            if last < 0:
                new_row.append(0)
            else:
                new_row.append(last)

            dp.append(new_row)

        return min(1, dp[query_row][query_glass])
