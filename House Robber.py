class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob, prev_no_rob = nums[0], 0
        n = len(nums)
        for i in range(1, n):
            prev_rob, prev_no_rob = prev_no_rob + nums[i], max(prev_no_rob, prev_rob)
        return max(prev_rob, prev_no_rob)

# class Solution:
#     def rob(self, nums) -> int:
#         if not nums:
#             return 0
#         dp = {'1': nums[0], '0': 0}
#         for idx, num in enumerate(nums[1:]):
#             idx += 1
#
#             for k in list(dp.keys()):
#                 if k[-1] == '0':
#                     # Choose to rob
#                     dp[k + '1'] = dp[k] + num
#
#                 # Choose not to rob
#                 dp[k + '0'] = dp[k]
#
#             # Only keep the most optimal results
#             dpa = {}
#             for last_record in ['0', '1']:
#                 dpa[last_record] = max([v for k, v in dp.items() if k[-1] == last_record])
#             dp = dpa
#
#         return max(dp.values())
#
# a = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
# b = Solution()
# print(b.rob(a))a

# Runtime: 28 ms, faster than 74.87% of Python3 online submissions for House Robber.
# Memory Usage: 14 MB, less than 9.09% of Python3 online submissions for House Robber.

# Time: O(n)
# Space: O(1)