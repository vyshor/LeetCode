class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        terms = {v: i for i, v in enumerate(nums)}
        parents = [i for i in range(n)]
        counts = [1] * n

        def find(i):
            nonlocal parents
            if parents[i] != i:
                return find(parents[i])
            return i

        def union(i, j):
            nonlocal parents, counts
            parent_i = find(i)
            parent_j = find(j)
            if parent_i != parent_j:
                parents[parent_i] = parent_j
                counts[parent_j] += counts[parent_i]
                counts[parent_i] = 0

        for i, num in enumerate(nums):
            nxt = num * num
            if nxt in terms:
                union(i, terms[nxt])

        maxx = max(counts)
        if maxx < 2:
            return -1
        return maxx

# class Solution:
#     def longestSquareStreak(self, nums: List[int]) -> int:
#         dp = set(nums)
#         maxx = -1
#         for num in set(nums):
#             if num not in dp:
#                 continue
#
#             length = 1
#             dp.remove(num)
#
#             left = num
#             while True:
#                 sqrt = int(math.sqrt(left))
#                 root = sqrt ** 2
#                 if root == left and sqrt in dp:
#                     left = sqrt
#                     length += 1
#                     dp.remove(sqrt)
#                 else:
#                     break
#
#             right = num
#             while True:
#                 sq = right ** 2
#                 if sq in dp:
#                     right = sq
#                     length += 1
#                     dp.remove(sq)
#                 else:
#                     break
#
#             if length > 1:
#                 maxx = max(maxx, length)
#         return maxx

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
