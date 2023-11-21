class Solution:
    def countAsterisks(self, s: str) -> int:
        opened = False
        count = 0
        for c in s:
            if c == "|":
                opened = not opened
            elif c == "*" and not opened:
                count += 1
        return count
