class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        left, right = 1, n
        lsum, rsum = 0, 0
        while lsum < rsum or left < right - 1:
            lsum += left
            left += 1
            if lsum > rsum:
                rsum += right
                right -= 1
        if lsum == rsum and left == right:
            return left
        return -1

