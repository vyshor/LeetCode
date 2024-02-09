class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        prev = s[0]
        count = 1
        total = 0

        for i in range(1, n):
            c = s[i]
            if c != prev:
                total += count * (count + 1) // 2
                prev = c
                count = 1
            else:
                count += 1

        total += count * (count + 1) // 2
        return total % MOD
