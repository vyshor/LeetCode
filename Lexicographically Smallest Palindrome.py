class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                c = min(s[i], s[j])
                s[i], s[j] = c, c
            i += 1
            j -= 1
        return ''.join(s)
