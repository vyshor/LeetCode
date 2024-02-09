class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        n1, n2 = len(word1), len(word2)
        s = ""
        while p1 < n1 and p2 < n2:
            s += word1[p1]
            s += word2[p2]
            p1 += 1
            p2 += 1

        if p1 < n1:
            s += word1[p1:]
        if p2 < n2:
            s += word2[p2:]

        return s
