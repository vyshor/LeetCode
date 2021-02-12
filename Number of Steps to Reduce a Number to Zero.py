class Solution:
    def numberOfSteps (self, num: int) -> int:
        op = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num = num // 2
            op += 1
        return op

# Time: O(lgn)
# Space: O(1)

# Runtime: 32 ms, faster than 63.53% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 14.3 MB, less than 5.45% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.