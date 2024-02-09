class Solution:
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slower = nums[0]
        while slower != slow:
            slow = nums[slow]
            slower = nums[slower]

        return slower

# class Solution:
#     def findDuplicate(self, nums):
#         n = len(nums)
#         ans = 0
#         for bitcount in range(32):
#             actual, expected = 0, 0
#             for i in range(n):
#                 actual += (nums[i] >> bitcount) % 2
#                 expected += (i >> bitcount) % 2
#             if actual > expected:
#                 ans |= 1 << bitcount
#
#         return ans
