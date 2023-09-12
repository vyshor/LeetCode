class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        h = 0
        for i in range(n - 1, -1, -1):
            if citations[i] >= n - i:
                h = max(h, n - i)

        return h
