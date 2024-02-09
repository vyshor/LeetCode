class Solution:
    def maxProduct(self, words: List[str]) -> int:
        pairs = []
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << ord(c) - 97
            pairs.append((mask, len(word)))

        n = len(pairs)
        maxx = 0
        for i in range(n):
            for j in range(i + 1, n):
                if pairs[i][0] & pairs[j][0] == 0:
                    maxx = max(maxx, pairs[i][1] * pairs[j][1])
        return maxx
