class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        n = len(s)
        m = len(g)
        i, j = 0, 0
        count = 0

        while j < m:
            while i < n and g[j] > s[i]:
                i += 1

            if i >= n:
                return count

            count += 1
            j += 1
            i += 1

        return count
