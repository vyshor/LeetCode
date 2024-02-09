class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = {}

        def assign(i, j, days):
            if (i, j, days) in dp:
                return dp[(i, j, days)]

            if days == 1:
                dp[(i, j, days)] = max(jobDifficulty[i:j + 1])
                return dp[(i, j, days)]

            # if j-i+1 < days:
            #     dp[(i, j, days)] = float('inf')
            #     return dp[(i, j, days)]

            if j - i + 1 == days:
                summ = 0
                for k in range(i, j + 1):
                    summ += jobDifficulty[k]
                dp[(i, j, days)] = summ
                return dp[(i, j, days)]
            else:
                minn = float('inf')
                for k in range(i, j):
                    if j - k + 1 < days - 1:
                        break

                    minn = min(minn, assign(i, k, 1) + assign(k + 1, j, days - 1))
                dp[(i, j, days)] = minn
                return dp[(i, j, days)]

        ans = assign(0, n - 1, d)
        # print(dp)
        return ans
