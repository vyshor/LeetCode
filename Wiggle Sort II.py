class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = sorted(nums)
        j = 0

        # n = 4
        # 0, 2
        # n-2 = 2

        # n = 3
        # 0, 2
        # n-1 = 2

        for i in range(n - 1 - (n % 2 == 0), -1, -2):
            nums[i] = arr[j]
            j += 1

        # n = 4
        # 1, 3
        # n-1 = 3

        # n = 3
        # 1
        # n-2 = 1

        for i in range(n - 1 - (n % 2), -1, -2):
            nums[i] = arr[j]
            j += 1
