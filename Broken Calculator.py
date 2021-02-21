class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        op = 0
        while Y > X:
            if Y % 2 == 1:
                Y += 1
                op += 1
            else:
                Y = Y// 2
                op += 1
        op += X - Y
        return op

# Time: O(lg(Y/X))
# Space: O(1)

# Runtime: 28 ms, faster than 86.05% of Python3 online submissions for Broken Calculator.
# Memory Usage: 14.3 MB, less than 47.18% of Python3 online submissions for Broken Calculator.