class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        nums = sorted(set(nums))

        m = len(nums)
        window = 1
        right = 0

        for left in range(m):
            while right < m and nums[right] < nums[left] + n:
                right += 1

            window = max(window, right - left)

        return n - window
