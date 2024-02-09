class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = [-num for num in nums]
        heapq.heapify(q)
        score = 0

        while k:
            num = heapq.heappop(q)
            score -= num
            heapq.heappush(q, math.floor(num / 3))
            k -= 1

        return score
