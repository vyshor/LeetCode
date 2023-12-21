class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = [point[0] for point in points]
        arr.sort()
        maxx = float('-inf')
        n = len(arr)
        for i in range(1, n):
            maxx = max(maxx, arr[i] - arr[i - 1])
        return maxx
