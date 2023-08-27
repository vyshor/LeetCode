class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        stones_set = {stone: i for i, stone in enumerate(stones)}

        dp = [set() for _ in range(n)]
        dp[0].add(0)

        for i, s in enumerate(dp):
            if i == n - 1:
                return bool(s)

            for k in s:
                for j in [k - 1, k, k + 1]:
                    if j <= 0:
                        continue
                    if stones[i] + j in stones_set:
                        dp[stones_set[stones[i] + j]].add(j)

