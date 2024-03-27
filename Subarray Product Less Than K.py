class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        n = len(nums)
        k = math.log(k)
        nums = [math.log(num) for num in nums]
        dp = [0] * (n + 1)
        summ = 0
        count = 0
        for i, num in enumerate(nums):
            summ += num
            dp[i + 1] = summ

        for i, num in enumerate(nums):
            remainder = k + dp[i]
            j = bisect.bisect_left(dp, remainder)
            if j < i + 1:
                continue

            count += j - i - 1

        return count
