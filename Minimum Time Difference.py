class Solution:
    def convert(self, s):
        t = int(s[:2]) * 60 + int(s[-2:])
        return t

    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        for tp in timePoints:
            arr.append(self.convert(tp))
        arr.sort()
        minn = arr[0] + 24 * 60 - arr[-1]
        for i in range(len(arr)-1):
            minn = min(minn, arr[i+1] - arr[i])
        return minn
