class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        n = 0
        for c in s:
            if c == "(":
                n += 1
            else:
                if n == 0:
                    count += 1
                else:
                    n -= 1
        return count + n
