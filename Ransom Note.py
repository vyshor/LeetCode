class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dp = collections.Counter(magazine)
        for c in ransomNote:
            if c not in dp or dp[c] == 0:
                return False
            else:
                dp[c] -= 1
        return True
