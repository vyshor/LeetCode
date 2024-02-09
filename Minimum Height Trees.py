class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        outdegrees = [0] * n
        dp = {}
        removed = 0
        removed_nodes = set()

        for edge in edges:
            a, b = edge

            outdegrees[a] += 1
            outdegrees[b] += 1

            if a not in dp:
                dp[a] = [b]
            else:
                dp[a].append(b)

            if b not in dp:
                dp[b] = [a]
            else:
                dp[b].append(a)

        while removed < n - 1:
            nodes = []
            for i, degree in enumerate(outdegrees):
                if degree == 1:
                    nodes.append(i)

            if removed + len(nodes) == n:
                return nodes

            for node in nodes:
                removed_nodes.add(node)
                outdegrees[node] = 0
                if node in dp:
                    for other_node in dp[node]:
                        outdegrees[other_node] -= 1

            removed += len(nodes)

        for i in range(n):
            if i not in removed_nodes:
                return [i]



