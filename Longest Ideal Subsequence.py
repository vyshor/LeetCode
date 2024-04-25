class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        largest = 0
        for c in s:
            pos = ord(c) - 97
            maxx = 1
            for i in range(max(0, pos-k), min(26, pos+k+1)):
                maxx = max(maxx, dp[i]+1)
            dp[pos] = maxx
            largest = max(largest, maxx)
        return largest
