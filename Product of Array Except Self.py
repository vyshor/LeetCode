class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp_left = [1] * n
        dp_right = [1] * n
        left = 1
        for i in range(n):
            left *= nums[i]
            dp_left[i] = left

        right = 1
        for i in range(n - 1, -1, -1):
            right *= nums[i]
            dp_right[i] = right

        ans = [1] * n
        for i in range(n):
            val = 1
            if i + 1 < n:
                val *= dp_right[i + 1]
            if i - 1 >= 0:
                val *= dp_left[i - 1]
            ans[i] = val
        return ans

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         L = []
#         R = []
#         pro = 1
#         for num in nums:
#             L.append(pro)
#             pro *= num
#
#         pro = 1
#         for idx in range(n - 1, -1, -1):
#             R.append(pro)
#             pro *= nums[idx]
#
#         for x in range(n):
#             L[x] = L[x] * R[n - 1 - x]
#         return L


# Time: O(n)
# Space: O(n)

# Runtime: 144 ms, faster than 42.03% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.4 MB, less than 84.00% of Python3 online submissions for Product of Array Except Self.
