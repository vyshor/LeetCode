class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = {}
        for (v, w) in items1:
            items[v] = w

        for (v, w) in items2:
            if v not in items:
                items[v] = w
            else:
                items[v] += w

        arr = []
        for k in sorted(list(items.keys())):
            arr.append([k, items[k]])
        return arr
