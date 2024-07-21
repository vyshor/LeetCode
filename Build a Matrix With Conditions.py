class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def condSort(conds, k):
            in_edges = [0] * k
            edges = {}
            for (fro, to) in conds:
                fro -= 1
                to -= 1
                if fro not in edges:
                    edges[fro] = set()

                if to not in edges[fro]:
                    edges[fro].add(to)
                    in_edges[to] += 1

            q = []
            for i in range(k):
                if in_edges[i] == 0:
                    q.append(i)
            order = []
            while q:
                i = q.pop()
                order.append(i)

                if i in edges:
                    for j in edges[i]:
                        in_edges[j] -= 1
                        if in_edges[j] == 0:
                            q.append(j)

            # print(in_edges, order)
            if len(order) < k:
                return {}

            dp = {}
            for i in range(k):
                dp[order[i]] = i
            return dp

        row = condSort(rowConditions, k)
        col = condSort(colConditions, k)
        # print(row, col)
        if len(row) == 0 or len(col) == 0:
            return []

        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            matrix[row[i]][col[i]] = i + 1
        return matrix
