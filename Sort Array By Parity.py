class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x % 2)

# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         even = []
#         odd = []
#         for n in A:
#             if n % 2:
#                 odd.append(n)
#             else:
#                 even.append(n)
#         return even + odd
#
#     # Time: O(n)
#     # Space: O(n)
