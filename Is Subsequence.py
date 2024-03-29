class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t and s:
            return False

        ns = len(s)
        nt = len(t)
        i, j = 0, 0
        while i < ns and j < nt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == ns


# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if not s:
#             return True
#         if not t and s:
#             return False
#
#         ns = len(s)
#         nt = len(t)
#         i, j = 0, 0
#         while i < ns and j < nt:
#             if s[i] == t[j]:
#                 i += 1
#                 j += 1
#             else:
#                 j += 1
#         return i == ns
