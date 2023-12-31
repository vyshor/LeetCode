class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        prev = {}
        maxx = -1
        for i, c in enumerate(s):
            if c not in prev:
                prev[c] = i
            else:
                maxx = max(maxx, i - prev[c] - 1)
        return maxx
