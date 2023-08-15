class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        edges = {}

        outdegree = [0] * n
        q = []
        ans = set()
        for i in range(n):
            outdegree[i] = len(graph[i])
            if outdegree[i] == 0:
                q.append(i)
                ans.add(i)

            for j in graph[i]:
                if j not in edges:
                    edges[j] = []
                edges[j].append(i)

        # print(q)
        # print(edges)

        visited = set()
        while q:
            # print(q, outdegree)
            i = q.pop()
            if i in visited:
                continue

            visited.add(i)
            if i in edges:
                for j in edges[i]:
                    outdegree[j] -= 1
                    if outdegree[j] == 0:
                        q.append(j)
                        ans.add(j)

        safe = []
        for i in range(n):
            if i in ans:
                safe.append(i)
        return safe



