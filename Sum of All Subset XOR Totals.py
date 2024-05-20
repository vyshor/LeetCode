class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        xor = 0
        def explore(i):
            nonlocal n, total, xor
            if i == n:
                total += xor
                return

            explore(i+1)

            prev = xor
            xor ^= nums[i]

            explore(i+1)
            xor = prev
        explore(0)
        return total

# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         total = 0
#         xor = 0
#         n = len(nums)
#
#         def xorNum(i):
#             nonlocal total, xor
#             if i == n:
#                 total += xor
#                 return
#
#             # Exclude current num
#             xorNum(i + 1)
#
#             # Include current num
#             prev = xor
#             xor ^= nums[i]
#             xorNum(i + 1)
#             xor = prev
#
#         xorNum(0)
#         return total
