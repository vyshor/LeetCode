class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dp = {}
        for idx, i in enumerate(nums):
            if dp.get(i) == None:
                dp[i] = idx
            else:
                if idx - dp[i] <= k:
                    return True
                else:
                    dp[i] = idx
        return False

# Runtime: 184 ms, faster than 6.52% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 21.6 MB, less than 35.10% of Python3 online submissions for Contains Duplicate II.
# Time: O(n)
# Space: O(n)
