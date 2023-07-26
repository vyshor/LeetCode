class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        dp = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 3):
            for i2 in range(i+1, n - 2):
                i3 = i2 + 1
                i4 = n - 1
                while i3 < i4:
                    total = nums[i] + nums[i2] + nums[i3] + nums[i4]
                    if total == target:
                        arr = [nums[i], nums[i2], nums[i3], nums[i4]]
                        if str(arr) not in dp:
                            ans.append(arr)
                            dp.add(str(arr))
                    if total <= target:
                        i3 += 1
                    else:
                        i4 -= 1
        return ans

