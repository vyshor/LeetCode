class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        arr = []

        def explore(i):
            nonlocal n, nums
            if i == n:
                subsets.append(list(arr))
                return

            explore(i + 1)

            arr.append(nums[i])
            explore(i + 1)
            arr.pop()

        explore(0)
        return subsets

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         ans = []
#         q = [((), 0)]
#         while q:
#             comb, i = q.pop()
#             if i == n:
#                 ans.append(comb)
#             else:
#                 q.append((comb, i + 1))
#                 q.append((comb + (nums[i],), i + 1))
#         return ans
