class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dp = {}
        ans = []

        for i, groupSize in enumerate(groupSizes):
            if groupSize not in dp:
                dp[groupSize] = [i]
            else:
                dp[groupSize].append(i)

            if len(dp[groupSize]) >= groupSize:
                ans.append(dp[groupSize])
                dp[groupSize] = []

        for group in dp.values():
            if group:
                ans.append(group)

        return ans

