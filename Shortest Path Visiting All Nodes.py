class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        q = deque([(1 << i, i, 0) for i in range(n)])
        visited = set()
        allReached = 2**n - 1

        while q:
            bitmask, i, length = q.popleft()
            for target in graph[i]:
                newBitMask = bitmask | (1 << target)
                if (target, newBitMask) in visited:
                    continue
                visited.add((target, newBitMask))
                if newBitMask == allReached:
                    return length+1
                q.append((newBitMask, target, length+1))
