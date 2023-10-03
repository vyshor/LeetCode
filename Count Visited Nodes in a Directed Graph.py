class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        dp = [0] * n

        for i in range(n):
            if dp[i]:
                continue

            k = i
            dist = 0
            path = {i: 0}
            while True:
                i = edges[i]
                dist += 1

                # Found loop
                if i in path:
                    loop = dist - path[i]
                    for j, d in path.items():
                        dp[j] = max(dist - d, loop)
                    break

                if i == -1:
                    dp[k] = dist - 1
                    break

                if dp[i]:
                    for j, d in path.items():
                        dp[j] = dist - d + dp[i]
                    break

                path[i] = dist

        return dp
