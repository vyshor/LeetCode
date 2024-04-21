class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        paths = {}
        for (u, v) in edges:
            if u not in paths:
                paths[u] = {v}
            else:
                paths[u].add(v)

            if v not in paths:
                paths[v] = {u}
            else:
                paths[v].add(u)

        q = deque([source])
        visited = {source}
        while q:
            i = q.popleft()
            if i not in paths:
                continue

            for dst in paths[i]:
                if dst in visited:
                    continue
                if dst == destination:
                    return True
                q.append(dst)
                visited.add(dst)
        return False
