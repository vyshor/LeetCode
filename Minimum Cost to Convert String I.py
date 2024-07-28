class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        edges = {}
        n = len(original)
        for i in range(n):
            c = original[i]
            c2 = changed[i]
            if c not in edges:
                edges[c] = {}

            if c2 not in edges[c]:
                edges[c][c2] = cost[i]
            else:
                edges[c][c2] = min(edges[c][c2], cost[i])

        dp = {}

        def get_cost(c1, c2):
            nonlocal edges, dp
            if (c1, c2) in dp:
                return dp[(c1, c2)]
            q = [(0, c1)]
            seen = set()
            while q:
                cost, pos = heapq.heappop(q)
                if pos == c2:
                    dp[(c1, c2)] = cost
                    return cost

                if pos in seen:
                    continue
                seen.add(pos)

                if pos in edges:
                    for c3, w in edges[pos].items():
                        heapq.heappush(q, (cost + w, c3))

            dp[(c1, c2)] = -1
            return -1

        m = len(source)
        total = 0
        for i in range(m):
            if source[i] != target[i]:
                cost = get_cost(source[i], target[i])
                if cost == -1:
                    return -1
                total += cost

        return total
