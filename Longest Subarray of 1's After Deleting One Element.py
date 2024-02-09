class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        deletion = 0
        ans = 0

        while right < n:
            if nums[right] == 1:
                ans = max(ans, right - left)
            else:
                deletion += 1
                while deletion > 1:
                    if nums[left] == 0:
                        deletion -= 1
                    left += 1

                ans = max(ans, right - left)

            right += 1

        return ans
