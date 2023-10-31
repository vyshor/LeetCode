class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        i = 0
        while i < n:
            if nums[i] != 0:
                if i+1 < n and nums[i] == nums[i+1]:
                    arr.append(nums[i]*2)
                    i += 2
                else:
                    arr.append(nums[i])
                    i += 1
            else:
                i += 1

        while len(arr) < n:
            arr.append(0)

        return arr
