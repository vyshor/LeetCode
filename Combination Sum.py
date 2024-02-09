class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        dp = [[] for _ in range(target + 1)]
        dp[target].append(())

        ans = []
        for j in range(n - 1, -1, -1):
            for i in range(target, -1, -1):
                if not dp[i]:
                    continue

                if i - candidates[j] < 0:
                    break

                for freq in dp[i]:
                    dp[i - candidates[j]].append(freq + (candidates[j],))

        return dp[0]
