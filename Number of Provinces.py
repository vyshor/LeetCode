class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        count = n

        def find(i):
            if parent[i] == i:
                return i
            else:
                indirect_parent = find(parent[i])
                parent[i] = indirect_parent
                return indirect_parent

        def union(i, j):
            nonlocal count

            parent_i = find(i)
            parent_j = find(j)
            if parent_i != parent_j:
                parent[parent_i] = parent_j
                count -= 1

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)

        return count
