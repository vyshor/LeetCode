class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        left, right = 0, 1
        prefix_sum = 0
        maxx = 1

        while right < n:
            prefix_sum += (right - left) * (nums[right] - nums[right - 1])
            while prefix_sum > k:
                prefix_sum -= nums[right] - nums[left]
                left += 1

            right += 1
            maxx = max(maxx, right - left)

        return maxx
