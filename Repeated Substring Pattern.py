class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        rotated = s
        for _ in range(n - 1):
            rotated = rotated[1:] + rotated[0]
            if s == rotated:
                return True
        return False


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
