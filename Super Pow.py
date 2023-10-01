class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return 1

        n = len(b)
        j = a
        ans = 1

        for i in range(n - 1, -1, -1):
            ans *= (j ** b[i]) % 1337
            j = (j ** 10) % 1337

        return ans % 1337

# 2 ^ 10
# 2 ^ 10 * 2 ^ 0

# 2 ^ 34
# (2 ^ 10)^3 * 2^4
# (j)^b[i] * (j)^b[i]