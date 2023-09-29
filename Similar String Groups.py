class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [i for i in range(n)]
        groups = n

        def compare(strA, strB):
            str_len = len(strA)
            diff = 0
            for i in range(str_len):
                diff += int(strA[i] != strB[i])
            return diff <= 2

        def find(i):
            nonlocal parent
            if parent[i] == i:
                return i
            else:
                j = i
                while parent[j] != j:
                    j = parent[j]

                k = i
                while parent[k] != k:
                    k, parent[k] = parent[k], j

                return j

        def union(i, j):
            nonlocal groups
            child = find(j)
            new_parent = find(i)
            if child != new_parent:
                parent[child] = new_parent
                groups -= 1

        for i in range(n):
            for j in range(i):
                if compare(strs[i], strs[j]):
                    union(i, j)

        return groups
