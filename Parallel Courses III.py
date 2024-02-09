class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegrees = [0] * n
        edges = {}

        for (prev, next) in relations:
            indegrees[next - 1] += 1
            if prev - 1 not in edges:
                edges[prev - 1] = [next - 1]
            else:
                edges[prev - 1].append(next - 1)

        q = []
        for i in range(n):
            if indegrees[i] == 0:
                heapq.heappush(q, (time[i], i))

        while q:
            t, i = heapq.heappop(q)
            if i in edges:
                for j in edges[i]:
                    indegrees[j] -= 1
                    if indegrees[j] == 0:
                        heapq.heappush(q, (t + time[j], j))

        return t
