class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        minn = 1
        left, right = 0, 1
        while right < n:
            if nums[right] > nums[left] + k:
                minn += 1
                left = right

            right += 1
        return minn
