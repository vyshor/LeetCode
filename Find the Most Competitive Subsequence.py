class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        size = len(nums)
        for idx, num in enumerate(nums):
            if len(ans) + (size - idx) <= k:
                ans += nums[idx:]
                break
            if not ans:
                ans.append(num)
            elif ans[-1] > num:
                while ans and ans[-1] > num and (len(ans) + (size - idx) > k):
                    ans.pop()
                ans.append(num)
            elif len(ans) < k:
                ans.append(num)

        return ans


# Runtime: 1348 ms, faster than 47.69% of Python3 online submissions for Find the Most Competitive Subsequence.
# Memory Usage: 27.5 MB, less than 39.71% of Python3 online submissions for Find the Most Competitive Subsequence.

# Time: O(n)
# Space: O(n)

from collections import deque

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = []
        ln = len(nums)
        for idx, num in enumerate(nums):
            q.append((num, idx, ln - idx))
        q.sort()
        q = deque(q)

        stack = []
        idx_lower = 0
        while k > 0:
            while True:
                num, idx, remaining = q.popleft()
                if idx >= idx_lower:
                    if k <= remaining:
                        ans.append(num)
                        idx_lower = idx+1
                        while len(stack):
                            q.appendleft(stack.pop())
                        break
                    else:
                        stack.append((num, idx, remaining))
            k -= 1
        return ans
