class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        ptrs = {k: [0] for k in dictionary}
        n = len(s)
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            c = s[i - 1]
            for word, all_pos in ptrs.items():
                new_pos = [0]
                for pos in all_pos:
                    if word[pos] == c:
                        pos += 1
                        if pos == len(word):
                            dp[i] = min(dp[i], dp[i - len(word)])
                        else:
                            new_pos.append(pos)
                ptrs[word] = new_pos
            # print(ptrs)

        # print(dp)
        return dp[-1]

# class Solution:
#     def minExtraChar(self, s: str, dictionary: List[str]) -> int:
#         n = len(s)
#         dp = [i for i in range(0, n + 1)]
#
#         for i in range(1, n + 1):
#             for word in dictionary:
#                 n_word = len(word)
#                 if i >= n_word and s[i - n_word:i] == word:
#                     dp[i] = min(dp[i], dp[i - n_word])
#             dp[i] = min(dp[i], dp[i - 1] + 1)
#
#         return dp[-1]

