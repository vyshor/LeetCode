class Solution:
    def maxDepth(self, s: str) -> int:
        open_count = 0
        maxx = 0
        for c in s:
            if c == "(":
                open_count += 1
                maxx = max(maxx, open_count)
            elif c == ")":
                open_count -= 1
        return maxx
