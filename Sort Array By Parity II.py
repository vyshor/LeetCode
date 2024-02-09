class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)

        even = 0
        while even < n and nums[even] % 2 == 0:
            even += 2

        for i in range(1, n, 2):
            if nums[i] % 2 == 0:
                nums[i], nums[even] = nums[even], nums[i]

                while even < n and nums[even] % 2 == 0:
                    even += 2

        return nums
