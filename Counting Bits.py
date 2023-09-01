class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0, 1]

        if n == 0:
            return dp[:1]
        elif n == 1:
            return dp

        start, end = 0, len(dp)
        for i in range(2, n + 1):
            if start < end:
                dp.append(dp[start] + 1)
                start += 1
            else:
                start, end = 0, len(dp)
                dp.append(dp[start] + 1)
                start += 1

        return dp
