class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 or k == 0:
            return

        total_swaps = 0
        i = 0
        while total_swaps < n:
            num = nums[i]
            j = i

            nums[(j + k) % n], num = num, nums[(j + k) % n]
            j = (j + k) % n
            total_swaps += 1

            while j != i:
                nums[(j + k) % n], num = num, nums[(j + k) % n]
                j = (j + k) % n
                total_swaps += 1

            i += 1


