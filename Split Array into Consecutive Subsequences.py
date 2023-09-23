class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {nums[0] + 1: [1]}
        for i in range(1, n):
            if nums[i] not in dp:
                next = nums[i] + 1
                if next not in dp:
                    dp[next] = [1]
                else:
                    heapq.heappush(dp[next], 1)
            else:
                count = heapq.heappop(dp[nums[i]])
                if len(dp[nums[i]]) == 0:
                    del dp[nums[i]]

                next = nums[i] + 1
                if next not in dp:
                    dp[next] = [count + 1]
                else:
                    heapq.heappush(dp[next], count + 1)

        # print(dp)

        for vals in dp.values():
            for val in vals:
                if val < 3:
                    return False

        return True

