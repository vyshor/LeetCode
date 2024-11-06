class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        i = 0
        count = 0
        while i < n:
            count += int(s[i] != s[i + 1])
            i += 2
        return count
