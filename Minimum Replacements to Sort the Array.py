class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[-1]
        count = 0

        for i in range(n - 2, -1, -1):
            num = nums[i]
            steps = (num - 1) // prev
            prev = num // (steps + 1)
            count += steps

        return count
