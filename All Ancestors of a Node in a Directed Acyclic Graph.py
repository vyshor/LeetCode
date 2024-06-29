class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        q = []
        in_edges = [0] * n
        pairs = {}
        for [u, v] in edges:
            if u not in pairs:
                pairs[u] = {v}
            else:
                pairs[u].add(v)
            in_edges[v] += 1

        for i, in_count in enumerate(in_edges):
            if in_count == 0:
                q.append(i)

        answer = [set() for _ in range(n)]
        while q:
            i = q.pop()
            if i in pairs:
                for target in pairs[i]:
                    answer[target].add(i)
                    answer[target].update(answer[i])
                    in_edges[target] -= 1
                    if in_edges[target] == 0:
                        q.append(target)

        answer = [sorted(v) for v in answer]
        return answer
