class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        arr = [-num for num in nums]
        heapq.heapify(arr)
        heapq.heapify(nums)
        return heapq.heappop(arr) * arr[0] - heapq.heappop(nums) * nums[0]
