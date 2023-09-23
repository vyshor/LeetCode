class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        dp = {}

        for num in nums:
            if counter[num] < 1:
                continue

            # Check if there is any existing subequence
            if num - 1 in dp:
                counter[num] -= 1
                if num in dp:
                    dp[num] += 1
                else:
                    dp[num] = 1

                dp[num - 1] -= 1
                if dp[num - 1] == 0:
                    del dp[num - 1]
            # No subsequence is found,
            # So check if a new sequence can be created
            elif counter[num + 1] and counter[num + 2]:
                counter[num] -= 1
                counter[num + 1] -= 1
                counter[num + 2] -= 1

                if num + 2 in dp:
                    dp[num + 2] += 1
                else:
                    dp[num + 2] = 1
            else:
                return False

        return True

# class Solution:
#     def isPossible(self, nums: List[int]) -> bool:
#         n = len(nums)
#         dp = {nums[0] + 1: [1]}
#         for i in range(1, n):
#             if nums[i] not in dp:
#                 next = nums[i] + 1
#                 if next not in dp:
#                     dp[next] = [1]
#                 else:
#                     heapq.heappush(dp[next], 1)
#             else:
#                 count = heapq.heappop(dp[nums[i]])
#                 if len(dp[nums[i]]) == 0:
#                     del dp[nums[i]]
#
#                 next = nums[i] + 1
#                 if next not in dp:
#                     dp[next] = [count + 1]
#                 else:
#                     heapq.heappush(dp[next], count + 1)
#
#         # print(dp)
#
#         for vals in dp.values():
#             for val in vals:
#                 if val < 3:
#                     return False
#
#         return True

