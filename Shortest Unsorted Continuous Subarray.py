class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 1
        start_idx = 0
        while start < len(nums):
            if nums[start] < nums[start - 1]:
                start_idx = start - 1
                break
            start += 1

        if start == len(nums):
            return 0

        end = len(nums) - 2
        end_idx = len(nums) - 1
        while end >= 0:
            if nums[end] > nums[end+1]:
                end_idx = end + 1
                break
            end -= 1

        _min = nums[start_idx]
        _max = nums[start_idx]
        for i in range(start_idx+1, end_idx+1):
            _min = min(_min, nums[i])
            _max = max(_max, nums[i])

        for i, num in enumerate(nums):
            if _min < num:
                start_idx = min(i, start_idx)
            if _max > num:
                end_idx = max(i, end_idx)

        ans = end_idx - start_idx + 1
        return ans if ans > 1 else 0

# Time: O(n)
# Space: O(1)

# Runtime: 244 ms, faster than 34.27% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 15.5 MB, less than 34.34% of Python3 online submissions for Shortest Unsorted Continuous Subarray.