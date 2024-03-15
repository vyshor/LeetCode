class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = ""
        for c in order:
            if c in counter:
                ans += c * counter[c]
                del counter[c]

        for c, count in counter.items():
            ans += c * count
        return ans
