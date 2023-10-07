class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        if n == 1:
            return 1

        edges = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                (x,y,r) = bombs[i]
                (x2, y2, r2) = bombs[j]

                y_dist = (y2-y)
                x_dist = (x2-x)
                dist_sq = x_dist*x_dist + y_dist*y_dist

                if dist_sq <= r*r:
                    edges[i].append(j)
                if dist_sq <= r2*r2:
                    edges[j].append(i)

        def exploreNode(i):
            nonlocal visited
            if i in visited:
                return 0

            visited.add(i)

            count = 1
            for j in edges[i]:
                if j in visited:
                    continue

                count += exploreNode(j)

            return count

        maxx = 0
        for i in range(n):
            visited = set()
            maxx = max(maxx, exploreNode(i))

        return maxx
