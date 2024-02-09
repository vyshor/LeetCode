class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dp = {}
        weights = {}
        n_edges = len(edges)

        for i, edge in enumerate(edges):
            a, b, w = edge
            dp[(a, b)] = i
            weights[(a, b)] = w

        def getWeight(weight_edges, excluded_idx, forced_idx):
            parent = list(range(n))

            def find(i):
                if parent[i] != i:
                    return find(parent[i])
                return i

            def union(i, j):
                parent[i] = j

            forced_edge = None

            q = []
            for i, edge in enumerate(weight_edges):
                if i == forced_idx:
                    forced_edge = (edge[2], edge[0], edge[1])

                if i == excluded_idx:
                    continue

                q.append((edge[2], edge[0], edge[1]))

            heapq.heapify(q)

            weight = 0
            total_connections = 0

            if forced_edge is not None:
                w, a, b = forced_edge
                union(find(a), find(b))
                weight += w
                total_connections += 1

            while q:
                w, a, b = heapq.heappop(q)

                ai = find(a)
                bi = find(b)

                if ai != bi:
                    union(ai, bi)
                    total_connections += 1
                    weight += w

            return weight, total_connections

        originalWeight, _ = getWeight(edges, -1, -1)
        critical = []
        pseudo = []

        for i in range(n_edges):
            criticalWeight, total_connections = getWeight(edges, i, -1)
            if criticalWeight > originalWeight or total_connections < n - 1:
                critical.append(i)
                continue

            pseudoWeight, _ = getWeight(edges, i, i)
            if pseudoWeight == originalWeight:
                pseudo.append(i)
                continue

        return [critical, pseudo]

