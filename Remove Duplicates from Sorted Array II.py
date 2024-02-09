class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        count = 1
        j = 1

        for i in range(1, n):
            if nums[i] == prev:
                if count < 2:
                    nums[j] = nums[i]
                    j += 1
                count += 1
            else:
                nums[j] = prev = nums[i]
                count = 1
                j += 1

        return j
