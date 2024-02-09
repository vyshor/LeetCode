class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        group = {}
        dp = {}

        def find(i):
            if i not in parent:
                parent[i] = i
                dp[i] = {i: 1.}
                group[i] = {i}

            if parent[i] == i:
                return i
            else:
                main_parent = find(parent[i])
                parent[i] = main_parent
                return main_parent

        def union(i, j, val):
            parent_i = find(i)
            parent_j = find(j)

            if parent_i == parent_j:
                return

            for prev_node in group[parent_i]:
                for next_node in group[parent_j]:
                    dp[prev_node][next_node] = dp[prev_node][i] * val * dp[j][next_node]
                    dp[next_node][prev_node] = 1 / dp[prev_node][next_node]

            parent[parent_j] = parent_i
            group[parent_i].update(group[parent_j])
            del group[parent_j]

        for i, (a, b) in enumerate(equations):
            union(a, b, values[i])

        ans = []
        for (a, b) in queries:
            if a in dp and b in dp[a]:
                ans.append(dp[a][b])
            else:
                ans.append(-1.)
        return ans
