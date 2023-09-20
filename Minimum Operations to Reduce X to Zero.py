class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        summ = 0
        left, right = 0, 0
        count = -1
        targetSum = sum(nums) - x

        while right < n:
            summ += nums[right]
            while summ > targetSum and left < n:
                summ -= nums[left]
                left += 1

            if summ == targetSum:
                count = max(count, right - left + 1)
            right += 1

        if count == -1:
            return count
        return n - count

# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         total = sum(nums)
#         nums_size = len(nums)
#         min_op = -1
#         sliding_ideal = total - x
#         sliding_sum = 0
#         start_pt = 0
#         end_pt = 0
#         while end_pt < nums_size:
#             sliding_sum += nums[end_pt]
#             end_pt += 1
#             if sliding_sum == sliding_ideal:
#                 used_size = nums_size - (end_pt - start_pt)
#                 if min_op == -1:
#                     min_op = used_size
#                 else:
#                     min_op = min(used_size, min_op)
#
#             while sliding_sum > sliding_ideal and start_pt < end_pt:
#                 sliding_sum -= nums[start_pt]
#                 start_pt += 1
#                 if sliding_sum == sliding_ideal:
#                     used_size = nums_size - (end_pt - start_pt)
#                     if min_op == -1:
#                         min_op = used_size
#                     else:
#                         min_op = min(used_size, min_op)
#         return min_op
#
# # Runtime: 1276 ms, faster than 51.43% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# # Memory Usage: 28.7 MB, less than 66.54% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
#
# # Time: O(n)
# # Space: O(1)
#
# from collections import deque
#
# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         start_pt = 0
#         end_pt = len(nums) - 1
#         if len(nums) == 1:
#             if x == nums[0]:
#                 return 1
#             else:
#                 return -1
#
#         q = deque([])
#         q.append((1, x - nums[start_pt], start_pt + 1, end_pt))
#         q.append((1, x - nums[end_pt], start_pt , end_pt - 1))
#         dp = set(((start_pt + 1, end_pt), (start_pt, end_pt - 1)))
#         while q:
#             op, new_x, s_pt, e_pt = q.popleft()
#             if new_x == 0:
#                 return op
#             elif s_pt < e_pt:
#                 if (s_pt + 1, e_pt) not in dp and new_x - nums[s_pt] >= 0:
#                     q.append((op + 1, new_x - nums[s_pt], s_pt + 1, e_pt))
#                     dp.add((s_pt + 1, e_pt))
#                 if (s_pt, e_pt - 1) not in dp and new_x - nums[e_pt] >= 0:
#                     q.append((op + 1, new_x - nums[e_pt], s_pt , e_pt - 1))
#                     dp.add((s_pt, e_pt - 1))
#         return -1
