class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        summ = 0
        for i in range(3*n - 2, n - 1, -2):
            summ += piles[i]
        return summ
