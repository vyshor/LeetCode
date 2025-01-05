class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        last_seen = {}
        ans = set()
        open_c = set()

        for i, c in enumerate(s):
            last_seen[c] = i

        for i, c in enumerate(s):
            if i < last_seen[c]:
                for cx in open_c:
                    ans.add(cx + c)

                open_c.add(c)
            else:
                if c in open_c:
                    open_c.remove(c)

                for cx in open_c:
                    ans.add(cx + c)

        # print(ans)
        return len(ans)

# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         n = len(s)
#         last = {}
#         seen = set()
#         pairs_opened = set()
#
#         for i, c in enumerate(s):
#             last[c] = i
#
#         for i, c in enumerate(s):
#             if last[c] == i and c in pairs_opened:
#                 pairs_opened.remove(c)
#
#             for c2 in pairs_opened:
#                 seen.add((c, c2))
#
#             if i < last[c]:
#                 pairs_opened.add(c)
#
#         return len(seen)
