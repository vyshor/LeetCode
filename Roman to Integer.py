class Solution:
    def romanToInt(self, s: str) -> int:
        dp = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        before = None
        for c in s:
            total += dp[c]
            if c in ["V", "X"]:
                if before == "I":
                    total -= 2
            elif c in ["L", "C"]:
                if before == "X":
                    total -= 20
            elif c in ["D", "M"]:
                if before == "C":
                    total -= 200
            before = c
        return total

# Time: O(n)
# Space: O(1)

# Runtime: 72 ms, faster than 10.76% of Python3 online submissions for Roman to Integer.
# Memory Usage: 14.2 MB, less than 85.09% of Python3 online submissions for Roman to Integer.