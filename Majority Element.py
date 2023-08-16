class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        major = nums[0]

        for i in range(1, n):
            if nums[i] == major:
                count += 1
            else:
                count -= 1
                if count == -1:
                    count = 1
                    major = nums[i]
        return major

