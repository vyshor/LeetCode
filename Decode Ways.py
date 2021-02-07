class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0" or "00" in s:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        prev_a = s[0]
        for idx, a in enumerate(s[1:]):
            idx += 2
            b = int(a)

            # Double digit
            if int(prev_a + a) <= 26 and prev_a != '0':
                if idx >= 2:
                    dp[idx] += dp[idx - 2]

            # Treat as single digit
            if int(a) > 0:
                dp[idx] += dp[idx - 1]
            prev_a = a

        return dp[len(s)] if len(s) > 1 else 1

# Runtime: 28 ms, faster than 86.08% of Python3 online submissions for Decode Ways.
# Memory Usage: 13.8 MB, less than 16.00% of Python3 online submissions for Decode Ways.

# Time: O(n)
# Space: O(n)