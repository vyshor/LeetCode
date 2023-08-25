class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True

        for i in range(1, n1 + 1):
            dp[i][0] = s1[i - 1] == s3[i - 1]
            if not dp[i][0]:
                break

        for j in range(1, n2 + 1):
            dp[0][j] = s2[j - 1] == s3[j - 1]
            if not dp[0][j]:
                break

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                top = i - 1 >= 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                left = j - 1 >= 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = top or left

                i -= 1
                if i <= 0:
                    break

        for j in range(1, n2 + 1):
            for i in range(n1, 0, -1):
                top = i - 1 >= 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                left = j - 1 >= 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = top or left

                j += 1
                if j > n2:
                    break

        return dp[n1][n2]
