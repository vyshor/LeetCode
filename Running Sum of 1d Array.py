class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ssum = 0
        ans = []
        for num in nums:
            ssum += num
            ans.append(ssum)
        return ans

# Time: O(n)
# Space: O(1)

# Runtime: 40 ms, faster than 62.06% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.3 MB, less than 90.17% of Python3 online submissions for Running Sum of 1d Array.
