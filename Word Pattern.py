class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        dp = {}
        visited = set()
        n = len(pattern)
        if len(words) != n:
            return False

        for i in range(n):
            c = pattern[i]
            word = words[i]
            if c in dp and dp[c] != word:
                return False

            if c not in dp:
                if word in visited:
                    return False

                dp[c] = word
                visited.add(word)

        return True
