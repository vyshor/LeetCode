class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        minn = n + 1
        window = 0
        while right < n:
            window += nums[right]
            right += 1

            if window >= target:
                minn = min(minn, right - left)

            while window - nums[left] >= target:
                window -= nums[left]
                left += 1
                minn = min(minn, right - left)

        if minn == n + 1:
            return 0

        return minn
