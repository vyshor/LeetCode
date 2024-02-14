class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr = []
        pos = True
        n = len(nums)
        i, j = 0, 0
        while nums[i] < 0:
            i += 1

        while nums[j] > 0:
            j += 1

        while i < n and j < n:
            if pos:
                arr.append(nums[i])
                i += 1
                while i < n and nums[i] < 0:
                    i += 1
            else:
                arr.append(nums[j])
                j += 1
                while j < n and nums[j] > 0:
                    j += 1
            pos = not pos

        if j < n:
            arr.append(nums[j])
        else:
            arr.append(nums[i])

        return arr
