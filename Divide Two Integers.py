class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = (abs(dividend) // abs(divisor)) * (-1 if dividend*divisor < 0 else 1)
        if -2**31 < ans <= 2**31 - 1:
            return ans
        elif ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return -2**31

# Runtime: 32 ms, faster than 76.88% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 14.2 MB, less than 83.72% of Python3 online submissions for Divide Two Integers.