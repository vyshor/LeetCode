class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if n == 1:
            return 1

        edges = {}
        ways = [0] * n
        ways[0] = 1
        dist = [float('inf')] * n
        dist[0] = 0

        for road in roads:
            u, v, t = road
            if u not in edges:
                edges[u] = [(v, t)]
            else:
                edges[u].append((v, t))

            if v not in edges:
                edges[v] = [(u, t)]
            else:
                edges[v].append((u, t))

        q = [(t, v, 1) for (v, t) in edges[0]]
        heapq.heapify(q)

        prev = -1
        expanding_nodes = set()

        while q:
            # print(q)
            # print(dist)
            # print(ways)

            t, v, way = heapq.heappop(q)
            if t < dist[v]:
                dist[v] = t
                ways[v] = way
            elif t == dist[v]:
                ways[v] += way
            else:
                continue

            expanding_nodes.add(v)
            prev = t

            if not q or q[0][0] > prev:
                for v in expanding_nodes:
                    for (v2, t2) in edges[v]:
                        if dist[v2] < t2 + dist[v]:
                            continue

                        heapq.heappush(q, (t2 + dist[v], v2, ways[v]))

                expanding_nodes = set()

        return ways[-1] % (10 ** 9 + 7)
