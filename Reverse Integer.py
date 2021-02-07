class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        if x < 0:
            neg = -1
            x *= -1
        else:
            neg = 1
        while x != 0:
            y = y * 10 + x % 10
            x = x // 10
        return y * neg if -2 ** 31 <= y * neg <= 2 ** 31 - 1 else 0

# Time Complexity: O(n) where n for the number of digits
# Space Complexity: O(1)
# Runtime: 28 ms, faster than 76.60% of Python3 online submissions for Reverse Integer.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Reverse Integer.