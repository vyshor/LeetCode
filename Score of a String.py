class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        n = len(s)
        prev = ord(s[0])
        for i in range(1, n):
            current = ord(s[i])
            score += abs(prev-current)
            prev = current
        return score
