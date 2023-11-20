class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edges = {}
        n = len(adjacentPairs) + 1
        for (a, b) in adjacentPairs:
            if a not in edges:
                edges[a] = {b}
            else:
                edges[a].add(b)

            if b not in edges:
                edges[b] = {a}
            else:
                edges[b].add(a)

        corner = 0
        for num, edge in edges.items():
            if len(edge) == 1:
                corner = num
                break

        arr = [corner, list(edges[corner])[0]]
        while len(arr) < n:
            for num in edges[arr[-1]]:
                if num != arr[-2]:
                    arr.append(num)
                    break
        return arr
