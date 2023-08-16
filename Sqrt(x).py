class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        start, end = 1, x
        while end > start + 1:
            mid = (start + end) // 2
            midsq = mid ** 2
            if midsq == x:
                return mid
            elif midsq < x:
                start = mid
            else:
                end = mid
        return start