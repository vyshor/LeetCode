class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        avgs = set()
        for i in range(n):
            j = n-i-1
            avgs.add((nums[i] + nums[j])/2)

        return len(avgs)
