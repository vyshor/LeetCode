class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        m = max(n // 4, 1)
        for i in range(n):
            if arr[i] == arr[i+m]:
                return arr[i]
