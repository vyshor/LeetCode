class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minn = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                minn = min(minn, abs(i - start))
        return minn

