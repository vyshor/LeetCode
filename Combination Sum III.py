class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dp = [[] for _ in range(n + 1)]
        dp[-1] = [()]

        for j in range(1, 10):
            for i in range(1, n + 1):
                if i - j < 0:
                    continue

                for comb in dp[i]:
                    if len(comb) + 1 > k:
                        continue

                    if i - j != 0:
                        dp[i - j].append(comb + (j,))
                    elif len(comb) == k - 1:
                        dp[i - j].append(comb + (j,))

        # print(dp)
        return dp[0]
