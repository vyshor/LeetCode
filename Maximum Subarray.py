class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        summ = 0
        left, right = 0, 0
        while right < n:
            summ += nums[right]
            ans = max(ans, summ)
            right += 1
            if summ < 0:
                left = right
                summ = 0
        return ans

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp = list(nums)
#         n = len(nums)
#
#         for i in range(1, n):
#             dp[i] = max(dp[i], dp[i - 1] + nums[i])
#
#         return max(dp)

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         L = []
#         R = []
#         pro = 0
#         for num in nums:
#             pro += num
#             L.append(pro)
#
#         pro = 0
#         for idx in range(n - 1, -1, -1):
#             pro += nums[idx]
#             R.append(pro)
#
#         L_id = L.index(min(L)) + 1
#         rR_id = R[::-1].index(min(R))
#         # rR_id = n - 1 - rR_id
#
#         print(L)
#         print(R[::-1])
#         print(L_id)
#         print(rR_id)
#         print(nums[L_id: rR_id])
#
#         if L_id > rR_id:
#             B = []
#             for x in range(n):
#                 B.append(L[x] + R[n - 1 - x])
#             return max([self.maxSubArray(nums[L_id:]), self.maxSubArray(nums[:rR_id])])
#
#         if L_id == rR_id:
#             return nums[L_id]
#         else:
#             return sum(nums[L_id: rR_id])
#
#
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_end = 0
#         max_far = 0
#         for num in nums:
#             max_end += num
#             if max_end > max_far:
#                 max_far = max_end
#             if max_end < 0:
#                 max_end = 0
#         if not max_far:
#             return max(nums)
#         else:
#             return max_far
#
# # Time: O(n)
# # Space: O(1)
# # Runtime: 76 ms, faster than 76.64% of Python3 online submissions for Maximum Subarray.
# # Memory Usage: 14.7 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.