class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        running_sum = sum(nums[:k])

        max_summ = running_sum
        for i in range(k, n+1):
            if running_sum > max_summ:
                max_summ = running_sum

            if i < n:
                running_sum += nums[i] - nums[i-k]

        return max_summ / k
