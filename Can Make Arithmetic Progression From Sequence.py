class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        diff = arr[1] - arr[0]
        for i in range(2, n):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True
