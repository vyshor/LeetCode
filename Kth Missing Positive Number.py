class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        for x in arr:
            if k > x - i - 1:
                k -= (x - i - 1)
                i = x
            else:
                return i + k
        return i + k

# Runtime: 36 ms, faster than 99.77% of Python3 online submissions for Kth Missing Positive Number.
# Memory Usage: 14.4 MB, less than 35.70% of Python3 online submissions for Kth Missing Positive Number.

# Time: O(n) for n being the size of arr
# Space: O(1)