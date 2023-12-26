class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {target: 1}

        for i in range(n):
            new_dp = {}
            for val, count in dp.items():
                for j in range(1, k + 1):
                    sub_val = val - j
                    if sub_val < 0:
                        break

                    if sub_val not in new_dp:
                        new_dp[sub_val] = count
                    else:
                        new_dp[sub_val] += count

            dp = new_dp
            # print(dp)

        return dp.get(0, 0) % MOD
