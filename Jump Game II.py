class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        end, next_end = 0, 0
        for i in range(n):
            if i > end:
                end = next_end
                count += 1

            next_end = max(next_end, nums[i] + i)

        return count

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         current_spot = 0
#         steps = 0
#         while current_spot < len(nums):
#             max_jump = 0
#             nxt_idx = 0
#             if current_spot + nums[current_spot] >= len(nums)-1:
#                 return steps + 1
#             for current_jump in range(nums[current_spot], 0, -1):
#                 jump = nums[current_spot + current_jump] + current_jump
#                 if jump > max_jump:
#                     max_jump = jump
#                     nxt_idx = current_spot + current_jump
#             current_spot = nxt_idx
#             steps += 1
#         return steps

# Time: O(n)
# Space: O(1)

# Runtime: 32 ms, faster than 68.19% of Python3 online submissions for Jump Game II.
# Memory Usage: 14.3 MB, less than 54.35% of Python3 online submissions for Jump Game II.
