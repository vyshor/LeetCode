class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        power = 1
        window = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                window += 1
                power = max(power, window)
            else:
                window = 1
        return power
