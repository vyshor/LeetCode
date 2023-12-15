class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        q = [-num for num in nums]
        heapq.heapify(q)
        return (heapq.heappop(q) + 1) * (q[0] + 1)
