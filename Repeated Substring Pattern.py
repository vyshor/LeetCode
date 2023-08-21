class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if s == 1:
            return False

        lps = [0] * n
        i, j = 0, 1
        while j < n:
            if s[i] == s[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i > 0:
                    i = lps[i - 1]
                else:
                    j += 1

        return lps[-1] and (n % (n - lps[-1]) == 0)

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         n = len(s)
#         rotated = s
#         for _ in range(n - 1):
#             rotated = rotated[1:] + rotated[0]
#             if s == rotated:
#                 return True
#         return False


# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         n = len(s)
#         if n == 1:
#             return False
#
#         for start in range(n//2+(n%2)):
#             if n % (start+1) == 0 and s[:start+1] * (n // (start+1)) == s:
#                 return True
#         return False
