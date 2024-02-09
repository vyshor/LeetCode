class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        lower = nums[0]+k
        upper = nums[-1]-k
        ans = nums[-1] - nums[0]

        for i in range(n-1):
            val_upper, val_lower = nums[i]+k, nums[i+1]-k
            ans = min(ans, max(upper, val_upper) - min(lower, val_lower))

        return ans
