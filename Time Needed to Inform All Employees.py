class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        edges = {i: [] for i in range(n)}
        for i, j in enumerate(manager):
            if j != -1:
                edges[j].append(i)

        q = deque([(0, headID)])
        dist = [float('inf')] * n

        while q:
            t, i = q.popleft()
            if dist[i] < t:
                continue

            dist[i] = t

            for j in edges[i]:
                if dist[j] > t + informTime[i]:
                    q.appendleft((t + informTime[i], j))

        return max(dist)

# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         edges = {i: [] for i in range(n)}
#         for i, j in enumerate(manager):
#             if j != -1:
#                 edges[j].append(i)
#
#         q = [(0, headID)]
#         count = 0
#         visited = set()
#
#         while q:
#             t, i = heapq.heappop(q)
#             if i in visited:
#                 continue
#
#             visited.add(i)
#             count += 1
#             if count == n:
#                 return t
#
#             for j in edges[i]:
#                 if j not in visited:
#                     heappush(q, (t + informTime[i], j))
