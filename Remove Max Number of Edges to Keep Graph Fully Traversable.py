class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(x, parents):
            if parents[x] != x:
                main_parent = find(parents[x], parents)
                parents[x] = main_parent
                return main_parent
            else:
                return x

        def union(x, y, parents):
            parent_x = find(x, parents)
            parent_y = find(y, parents)
            if parent_x == parent_y:
                return 1, 0
            else:
                parents[parent_y] = parent_x
                return 0, 1

        parents = [i for i in range(n)]
        count = 0
        islands = n
        for (t, u, v) in edges:
            if t == 3:
                count_inc, island_dec = union(u - 1, v - 1, parents)
                count += count_inc
                islands -= island_dec

        parents_2 = list(parents)
        islands2 = islands
        for (t, u, v) in edges:
            if t == 1:
                count_inc, island_dec = union(u - 1, v - 1, parents)
                count += count_inc
                islands -= island_dec

            elif t == 2:
                count_inc, island_dec = union(u - 1, v - 1, parents_2)
                count += count_inc
                islands2 -= island_dec

        if islands2 != 1 or islands != 1:
            return -1

        return count
