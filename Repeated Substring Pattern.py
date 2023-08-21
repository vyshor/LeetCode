class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        for start in range(n//2+(n%2)):
            if n % (start+1) == 0 and s[:start+1] * (n // (start+1)) == s:
                return True
        return False
