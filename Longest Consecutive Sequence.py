class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        parents = [i for i in range(n)]
        size = [1] * n
        max_size = 1
        nums_set = {}

        def find(x):
            if parents[x] == x:
                return x

            return find(parents[x])

        def union(x, y):
            nonlocal max_size
            parent_y = find(y)
            parent_x = find(x)
            parents[parent_x] = find(parent_y)
            size[parent_y] += size[parent_x]
            max_size = max(max_size, size[parent_y])

        for i, num in enumerate(nums):
            if num in nums_set:
                continue

            if num + 1 in nums_set:
                union(i, nums_set[num + 1])
                nums_set[num] = find(i)

            if num - 1 in nums_set:
                union(i, nums_set[num - 1])

            nums_set[num] = find(i)

        # print(parents)
        # print(size)
        return max_size

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         dp = {}
#         if not nums:
#             return 0
#         max_len = 1
#         for num in nums:
#             if not dp.get(num):
#                 dp[num] = True
#         for num in nums:
#             if dp[num]:
#                 temp_num = 1
#                 orig_num = num
#                 num += 1
#                 while dp.get(num, False):
#                     dp[num] = False
#                     num += 1
#                     temp_num += 1
#                     max_len = max(temp_num, max_len)
#
#                 num = orig_num - 1
#                 while dp.get(num, False):
#                     dp[num] = False
#                     num -= 1
#                     temp_num += 1
#                     max_len = max(temp_num, max_len)
#         return max_len

# Time:  O(n) for n the number of elements in list - two way transverse, and only look once when searching
# Space: O(n) for everything in a hashtable/dict

# Runtime: 64 ms, faster than 80.11% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Longest Consecutive Sequence.