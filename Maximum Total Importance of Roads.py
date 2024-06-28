class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0] * n
        for (u, v) in roads:
            arr[u] += 1
            arr[v] += 1

        arr.sort(reverse=True)
        summ = 0
        for num in arr:
            summ += n * num
            n -= 1
        return summ
