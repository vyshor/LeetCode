class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = {}
        for (fro, to, w) in edges:
            if fro not in dp:
                dp[fro] = {}

            if to not in dp:
                dp[to] = {}

            dp[fro][to] = w
            dp[to][fro] = w

        def explore(i):
            nonlocal dp
            visited = set()
            node_dist = [float('inf')] * n
            count = 0
            q = [(0, i)]
            while q:
                dist, j = heapq.heappop(q)
                if dist > distanceThreshold:
                    return count

                if j in visited:
                    continue

                visited.add(j)
                count += 1
                if j in dp:
                    for target in dp[j]:
                        if target in visited:
                            continue

                        if dist + dp[j][target] <= distanceThreshold:
                            heapq.heappush(q, (dist + dp[j][target], target))
            return count

        minn = float('inf')
        idx = 0
        for i in range(n):
            cities = explore(i)
            if cities <= minn:
                idx = i
                minn = cities
        return idx
