class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        n = len(happiness)
        count = 0
        for i in range(k):
            count += max(0, happiness[n-i-1]-i)
        return count
