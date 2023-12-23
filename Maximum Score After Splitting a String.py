class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left, right = int(s[0] == "0") , 0
        for i in range(1, n):
            right += int(s[i] == "1")

        maxx = left+right
        for i in range(1, n-1):
            left += int(s[i] == "0")
            right -= int(s[i] == "1")
            maxx = max(maxx, left+right)

        return maxx
