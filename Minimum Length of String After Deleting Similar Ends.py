class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1

        while s[i] == s[j] and i != j:
            c = s[i]
            i += 1
            while i <= j and s[i] == c:
                i += 1

            j -= 1
            while j >= i and s[j] == c:
                j -= 1

            if j < i:
                return 0

        return j - i + 1
