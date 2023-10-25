class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        smallest = []
        minn = nums[0]
        for i in range(n):
            minn = min(minn, nums[i])
            smallest.append(minn)

        maxx = nums[-1]
        for i in range(n-1, -1, -1):
            if nums[i] < maxx and nums[i] > smallest[i]:
                return True

            maxx = max(maxx, nums[i])

        return False
