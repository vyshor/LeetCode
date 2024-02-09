class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxx = nums[k]
        minn = nums[k]
        left, right = k - 1, k + 1
        while left >= 0 and right <= n - 1:
            if nums[left] >= nums[right]:
                minn = min(nums[left], minn)
                maxx = max(maxx, (right - left) * minn)
                left -= 1
            else:
                minn = min(nums[right], minn)
                maxx = max(maxx, (right - left) * minn)
                right += 1

        while left >= 0:
            minn = min(nums[left], minn)
            maxx = max(maxx, (right - left) * minn)
            left -= 1

        while right <= n - 1:
            minn = min(nums[right], minn)
            maxx = max(maxx, (right - left) * minn)
            right += 1

        return maxx
