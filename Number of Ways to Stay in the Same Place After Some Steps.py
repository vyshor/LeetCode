class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}

        def findWays(i, steps_left):
            if not (0 <= i < arrLen):
                return 0
            elif steps_left == 0:
                return 1 if i == 0 else 0
            elif abs(steps_left) == i:
                return 1

            if (i, steps_left) in dp:
                return dp[(i, steps_left)]

            right = findWays(i + 1, steps_left - 1)
            left = findWays(i - 1, steps_left - 1)
            mid = findWays(i, steps_left - 1)

            dp[(i, steps_left)] = (right + left + mid) % MOD

            return dp[(i, steps_left)]

        ans = findWays(0, steps) % MOD
        # print(dp)
        return ans
