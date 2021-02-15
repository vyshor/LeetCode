class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        explored = set()

        def visit(node, current_dist, visited, explored):
            visited[node] = current_dist
            explored.add(node)
            for nxt_node in graph[node]:
                if nxt_node in visited:
                    if (current_dist + visited[nxt_node] + 1) % 2 != 0:
                        return False
                else:
                    if not visit(nxt_node, current_dist+1, visited, explored):
                        return False
            return True


        for u, nx in enumerate(graph):
            if u not in explored:
                visited = {}
                if not visit(u, 0, visited, explored):
                    return False

        return True

# Time: O(V+E)
# Space: O(V+E)

# Runtime: 176 ms, faster than 63.50% of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 15 MB, less than 24.18% of Python3 online submissions for Is Graph Bipartite?.