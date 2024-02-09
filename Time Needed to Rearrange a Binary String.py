class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        dist = []

        j = 0
        has1 = False
        for i, c in enumerate(s):
            if c == "1":
                dist.append(i - j)
                j += 1
                has1 = True

        if not has1:
            return 0

        n = len(dist)
        for i in range(1, n):
            if dist[i] != 0:
                dist[i] = max(dist[i], dist[i - 1] + 1)

        return max(dist)
