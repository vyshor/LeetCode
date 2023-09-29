class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            dp = {}
            visited = set()
            valid_word = True

            for i, c in enumerate(word):
                if c in dp:
                    if dp[c] != pattern[i]:
                        valid_word = False
                        break
                else:
                    if pattern[i] in visited:
                        valid_word = False
                        break

                    visited.add(pattern[i])
                    dp[c] = pattern[i]

            if valid_word:
                ans.append(word)
        return ans
