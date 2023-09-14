# import numpy as np

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[n] * n for _ in range(3)]

        for i in range(1, 4):
            dp[i - 1][0] = int(nums[0] != i)

        for i in range(1, n):
            for j in range(1, 4):
                if nums[i] == j:  # 2,2
                    for k in range(j, 0, -1):
                        dp[j - 1][i] = min(dp[j - 1][i], dp[k - 1][i - 1])
                elif nums[i] < j:  # 1,2
                    dp[j - 1][i] = min(dp[j - 1][i], dp[j - 1][i - 1] + 1)
                else:  # 3, 2
                    dp[j - 1][i] = min(dp[j - 1][i], dp[j - 1][i - 1] + 1)

        # print(np.matrix(dp))
        return min([dp[i][-1] for i in range(3)])



