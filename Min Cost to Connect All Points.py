class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        q = []
        dist = 0
        join_count = 0

        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i != j:
                    (x1, y1) = p1
                    (x2, y2) = p2
                    q.append((abs(x1 - x2) + abs(y1 - y2), i, j))

        def find(i):
            j = i
            while parent[j] != j:
                j = parent[j]

            while i != j:
                parent[i] = j
                i = parent[i]

            return j

        def union(i, j, d):
            nonlocal dist, join_count
            parent_i = find(i)
            parent_j = find(j)
            if parent_i == parent_j:
                return

            dist += d
            join_count += 1
            parent[parent_i] = parent_j

        heapq.heapify(q)
        while join_count < n - 1:
            d, i, j = heapq.heappop(q)
            union(i, j, d)

        return dist

