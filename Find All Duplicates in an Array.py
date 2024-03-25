class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for num in nums:
            num = num % n
            if num == 0:
                num = n
            if nums[num-1] > n:
                ans.append(num)
            else:
                nums[num-1] += n
        return ans

# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#
#         ans = []
#         for i in range(n):
#             nums[(nums[i]-1)%(n+1)] += (n+1)
#         for i in range(n):
#             if nums[i] // (n+1) == 2:
#                 ans.append(i+1)
#         return ans
