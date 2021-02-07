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