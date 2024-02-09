class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dp = {c: i for (i, c) in enumerate(order)}
        dp['`'] = -1
        words = [word + '`' for word in words]

        def key(strA, strB):
            nA, nB = len(strA), len(strB)
            i = 0
            n = max(nA, nB)
            while i < n:
                if dp[strA[i]] < dp[strB[i]]:
                    return -1
                elif dp[strA[i]] > dp[strB[i]]:
                    return 1
                i += 1
            return 0

        return words == sorted(words, key=functools.cmp_to_key(key))

# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         dp = {}
#         for i, c in enumerate(order):
#             dp[c] = i
#
#         def compareWords(a, b):
#             for idx, _a in enumerate(a):
#                 if idx >= len(b) or dp[_a] > dp[b[idx]]:
#                     return False
#                 elif dp[_a] < dp[b[idx]]:
#                     return True
#             return True
#
#         wordA = words[0]
#         for i in range(1, len(words)):
#             wordB = words[i]
#             if not compareWords(wordA, wordB):
#                 return False
#             else:
#                 wordA = wordB
#         return True

# Runtime: 36 ms, faster than 62.27% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 14.3 MB, less than 47.70% of Python3 online submissions for Verifying an Alien Dictionary.

# Time: O(n+m)
# Space: O(1)
