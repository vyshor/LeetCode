class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        maxx = stones[1]

        for i in range(2, n):
            maxx = max(maxx, stones[i] - stones[i - 2])

        return maxx
