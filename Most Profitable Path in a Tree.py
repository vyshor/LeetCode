class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        connected = {}

        for a, b in edges:
            if a not in connected:
                connected[a] = [b]
            else:
                connected[a].append(b)

            if b not in connected:
                connected[b] = [a]
            else:
                connected[b].append(a)

        bob_path = []
        all_leaf_paths = []

        def dfs(prev, node, path):
            nonlocal bob_path
            if node == bob:
                bob_path = list(path)
                bob_path.append(bob)

            # Leaf
            if len(connected[node]) == 1 and node != 0:
                path.append(node)
                all_leaf_paths.append(tuple(path))
                path.pop()
                return

            path.append(node)
            for next_node in connected[node]:
                if next_node != prev:
                    dfs(node, next_node, path)
            path.pop()

        dfs(-1, 0, [])
        # print(all_leaf_paths)
        # print(bob_path)
        bob_opened = {}
        m = len(bob_path)
        j = 0
        for i in range(m-1, -1, -1):
            bob_opened[bob_path[i]] = j
            j += 1

        maxx = float('-inf')
        for leaf_path in all_leaf_paths:
            j = 0
            total_cost = 0
            for node in leaf_path:
                if node in bob_opened:
                    if j == bob_opened[node]:
                        total_cost += amount[node] // 2
                    elif j < bob_opened[node]:
                        total_cost += amount[node]
                else:
                    total_cost += amount[node]
                j += 1

            maxx = max(maxx, total_cost)

        return maxx
