class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp = set(nums)
        maxx = -1
        for num in set(nums):
            if num not in dp:
                continue

            length = 1
            dp.remove(num)

            left = num
            while True:
                sqrt = int(math.sqrt(left))
                root = sqrt ** 2
                if root == left and sqrt in dp:
                    left = sqrt
                    length += 1
                    dp.remove(sqrt)
                else:
                    break

            right = num
            while True:
                sq = right ** 2
                if sq in dp:
                    right = sq
                    length += 1
                    dp.remove(sq)
                else:
                    break

            if length > 1:
                maxx = max(maxx, length)
        return maxx

# class Solution:
#     def longestSquareStreak(self, nums: List[int]) -> int:
#         nums.sort()
#         dp = {}
#         maxx = -1
#         for num in nums:
#             sqrt = int(math.sqrt(num))
#             root = sqrt ** 2
#             if root == num and sqrt in dp:
#                 dp[num] = dp[sqrt] + 1
#                 maxx = max(maxx, dp[num])
#             else:
#                 dp[num] = 1
#         return maxx
