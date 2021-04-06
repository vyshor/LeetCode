# odd
# x = n // 2
# x(x+1)
# even
# x = n // 2
# x^2

class Solution:
    def minOperations(self, n: int) -> int:
        return (n // 2)*(n // 2 + n % 2)

# Runtime: 28 ms, faster than 91.63% of Python3 online submissions for Minimum Operations to Make Array Equal.
# Memory Usage: 14 MB, less than 90.00% of Python3 online submissions for Minimum Operations to Make Array Equal.

# Time: O(1)
# Space: O(1)
