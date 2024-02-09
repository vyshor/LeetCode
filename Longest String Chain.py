class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        length = {}
        for word in words:
            n = len(word)
            dp[word] = 1
            if n not in length:
                length[n] = [word]
            else:
                length[n].append(word)

        keys = sorted(length.keys())
        ans = 1
        for l in keys:
            for word in length[l]:
                n = len(word)
                for i in range(n):
                    shorten_word = word[:i] + word[i+1:]
                    if shorten_word in dp:
                        dp[word] = max(dp[word], dp[shorten_word] + 1)
                        ans = max(ans, dp[word])

        # print(dp)
        return ans

# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         if not words:
#             return 0
#         words.sort(key=len)
#         dp = {}
#         max_comb = 1
#         for word in words:
#             dp[word] = 1
#             for i in range(len(word)):
#                 prev_word = word[:i] + word[i+1:]
#                 if prev_word in dp:
#                     dp[word] = dp[prev_word] + 1
#                     max_comb = max(max_comb, dp[word])
#         return max_comb

# Tiem: O(nlgn + nM) for n number of words, M for longest length of word
# Space: O(nM)

# Runtime: 124 ms, faster than 89.97% of Python3 online submissions for Longest String Chain.
# Memory Usage: 14.7 MB, less than 75.27% of Python3 online submissions for Longest String Chain.


