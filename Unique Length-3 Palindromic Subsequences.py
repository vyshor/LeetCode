class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        last = {}
        seen = set()
        pairs_opened = set()

        for i, c in enumerate(s):
            last[c] = i

        for i, c in enumerate(s):
            if last[c] == i and c in pairs_opened:
                pairs_opened.remove(c)

            for c2 in pairs_opened:
                seen.add((c, c2))

            if i < last[c]:
                pairs_opened.add(c)

        return len(seen)
