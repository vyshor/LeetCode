class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxx = []
        q = deque()

        for idx, num in enumerate(nums):
            if q and q[0] == idx - k:
                q.popleft()

            while q and num > nums[q[-1]]:
                q.pop()

            q.append(idx)

            if idx >= k - 1:
                maxx.append(nums[q[0]])
        return maxx

# Runtime: 332 ms, faster than 82.99% of Python3 online submissions for Sliding Window Maximum.
# Memory Usage: 26.5 MB, less than 27.90% of Python3 online submissions for Sliding Window Maximum.
# Time: O(n)
# Space: O(k)

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         q = [-1 * num for num in nums[:k-1]]
#
#         heapq.heapify(q)
#         sliding = {}
#
#         for num in q:
#             if num not in sliding:
#                 sliding[num] = 1
#             else:
#                 sliding[num] += 1
#
#         ans = []
#         for i in range(k-1, n):
#             num = nums[i] * -1
#             heapq.heappush(q, num)
#
#             # print(q)
#
#             if num not in sliding:
#                 sliding[num] = 1
#             else:
#                 sliding[num] += 1
#
#             maxx = q[0]
#             while maxx not in sliding:
#                 heapq.heappop(q)
#                 maxx = q[0]
#
#             if maxx in sliding:
#                 ans.append(maxx * -1)
#
#             # print(sliding)
#
#             prev = nums[i-k+1] * -1
#             sliding[prev] -= 1
#             if sliding[prev] == 0:
#                 del sliding[prev]
#
#             maxx = q[0]
#             while maxx not in sliding:
#                 heapq.heappop(q)
#
#                 if not q:
#                     break
#                 maxx = q[0]
#
#         return ans
