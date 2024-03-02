class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        arr = []
        sq_i, sq_j = nums[i] * nums[i], nums[j] * nums[j]
        while i < j:
            if sq_i > sq_j:
                arr.append(sq_i)
                i += 1
                sq_i = nums[i] * nums[i]
            else:
                arr.append(sq_j)
                j -= 1
                sq_j = nums[j] * nums[j]

        arr.append(sq_i)
        return arr[::-1]
