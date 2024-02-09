class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # Base case, each index needs to have at least 1
        maxSum -= n
        num = 1
        left, right = index, index
        while right != n-1 or left != 0:
            if maxSum >= (right-left+1):
                maxSum -= (right-left+1)
                right = min(right+1, n-1)
                left = max(left-1, 0)
                num += 1
            else:
                return num

        return num + (maxSum // n)

