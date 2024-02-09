class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        count = 0
        dp = {nums[0], nums[1]}

        for i in range(2, n):
            prev = nums[i] - diff
            prev2 = nums[i] - 2 * diff
            if prev in dp and prev2 in dp:
                count += 1

            dp.add(nums[i])
        return count
