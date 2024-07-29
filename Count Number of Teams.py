class Solution:
    def countTriplets(self, arr):
        dp = []
        count = 0
        for num in arr:
            i = bisect.bisect_left(dp, (num, 0))
            for j in range(i):
                count += dp[j][1]
            dp.insert(i, (num, i))
        return count

    def numTeams(self, rating: List[int]) -> int:
        return self.countTriplets(rating) + self.countTriplets(rating[::-1])
