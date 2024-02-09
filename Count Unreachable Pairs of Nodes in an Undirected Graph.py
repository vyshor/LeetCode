class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        groups = {i: 1 for i in range(n)}
        count = n * (n - 1) // 2

        def find(i):
            nonlocal parents

            if parents[i] == i:
                return i

            parent = find(parents[i])
            parents[i] = parent
            return parent

        def union(i, j):
            nonlocal parents, groups

            i_parent = find(i)
            j_parent = find(j)
            if i_parent != j_parent:
                parents[i_parent] = j_parent
                groups[j_parent] += groups[i_parent]
                del groups[i_parent]

        for edge in edges:
            (i, j) = edge
            union(i, j)

        for i in groups.values():
            count -= i * (i - 1) // 2

        return count
