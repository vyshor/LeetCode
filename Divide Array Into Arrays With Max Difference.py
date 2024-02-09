class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        for i in range(0, n, 3):
            if nums[i + 2] - nums[i] > k:
                return []

        ans = []
        arr = []
        for num in nums:
            arr.append(num)
            if len(arr) == 3:
                ans.append(arr)
                arr = []
        return ans
