class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        q = [-target]
        dp = {-target: 1}
        ans = 0

        while q:
            v = heapq.heappop(q)
            count = dp[v]

            for num in nums:
                summ = num + v
                if summ < 0:
                    if summ not in dp:
                        dp[summ] = count
                        heapq.heappush(q, summ)
                    else:
                        dp[summ] += count

                elif summ == 0:
                    ans += count

        return ans

# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         try:
#             nums = [x for x in nums if x <= target]
#             dp = [0] * (target + 1)
#             for num in nums:
#                 dp[num] = 1
#
#             for i in range(target + 1):
#                 for num in nums:
#                     if i - num >= 0:
#                         dp[i] += dp[i - num]
#             return dp[target]
#         except:
#             return 0


# Runtime: 36 ms, faster than 94.47% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.1 MB, less than 22.22% of Python3 online submissions for Combination Sum IV.

# Time: O(value of target* size of nums)
# Space: O(value of target)