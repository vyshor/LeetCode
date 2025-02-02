class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        parity = nums[0] & 1
        for i in range(1, n):
            new_parity = nums[i] & 1
            if new_parity == parity:
                return False
            parity = new_parity
        return True
