class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        dp = {}
        for i, [u, v] in enumerate(edges):
            prob = succProb[i]
            if u not in dp:
                dp[u] = {}
            if v not in dp:
                dp[v] = {}
            dp[u][v] = prob
            dp[v][u] = prob

        visited = set()
        q = [(-1., start_node)]
        while q:
            prob, node = heapq.heappop(q)
            if node == end_node:
                return -prob

            if node in visited:
                continue
            visited.add(node)
            if node not in dp:
                continue

            for other, cost in dp[node].items():
                if other not in visited:
                    heapq.heappush(q, (cost * prob, other))
        return 0.

# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
#         directions = {}
#         for i, edge in enumerate(edges):
#             (fro, to) = edge
#             if fro not in directions:
#                 directions[fro] = [(to, succProb[i])]
#             else:
#                 directions[fro].append((to, succProb[i]))
#
#             if to not in directions:
#                 directions[to] = [(fro, succProb[i])]
#             else:
#                 directions[to].append((fro, succProb[i]))
#
#         q = deque([(start_node, 1.)])
#         dist = [0.] * n
#         dist[start_node] = 1.
#         ans = 0
#
#         while q:
#             i, prob = q.popleft()
#             if prob < ans:
#                 continue
#
#             if i in directions:
#                 for (to, subProb) in directions[i]:
#                     if to == end_node:
#                         ans = max(ans, prob*subProb)
#                     elif dist[to] < prob*subProb:
#                         q.append((to, prob*subProb))
#                         dist[to] = prob*subProb
#
#         return ans

# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
#         directions = {}
#         for i, edge in enumerate(edges):
#             (fro, to) = edge
#             if fro not in directions:
#                 directions[fro] = [(to, succProb[i])]
#             else:
#                 directions[fro].append((to, succProb[i]))
#
#             if to not in directions:
#                 directions[to] = [(fro, succProb[i])]
#             else:
#                 directions[to].append((fro, succProb[i]))
#
#         q = [(start_node, -1.)]
#         dist = [0.] * n
#         dist[start_node] = 1.
#         ans = 0
#
#         while q:
#             i, prob = heapq.heappop(q)
#             prob *= -1
#
#             if prob < ans:
#                 continue
#
#             if i in directions:
#                 for (to, subProb) in directions[i]:
#                     if to == end_node:
#                         ans = max(ans, prob*subProb)
#
#                     elif dist[to] < prob*subProb:
#                         heapq.heappush(q, (to, -prob*subProb))
#                         dist[to] = prob*subProb
#
#         return ans

