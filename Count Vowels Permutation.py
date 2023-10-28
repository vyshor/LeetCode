class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}
        next_opts = {
            "": ['a', 'e', 'i', 'o', 'u'],
            "a": ['e'],
            "e": ['a', 'i'],
            "i": ['a', 'e', 'o', 'u'],
            "o": ['i', 'u'],
            "u": ['a'],
        }

        def findComb(prev, count):
            if count == 0:
                return 1

            if (prev, count) in dp:
                return dp[(prev, count)]

            factor = 0
            for c in next_opts[prev]:
                factor += findComb(c, count - 1)
            dp[(prev, count)] = factor % MOD
            return dp[(prev, count)]

        ans = findComb("", n) % MOD
        # print(dp)
        return ans
