class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [i for i in range(0, n + 1)]

        for i in range(1, n + 1):
            for word in dictionary:
                n_word = len(word)
                if i >= n_word and s[i - n_word:i] == word:
                    dp[i] = min(dp[i], dp[i - n_word])
            dp[i] = min(dp[i], dp[i - 1] + 1)

        return dp[-1]

