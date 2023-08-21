class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatAll(k):
            t = 0
            for pile in piles:
                t += pile // k + (pile % k != 0)
            return t

        start, end = 1, max(piles) + 1
        mink = end

        while start <= end:
            mid = (start + end) // 2
            t = eatAll(mid)

            if t <= h:
                mink = min(mink, mid)

            if start == end - 1:
                break

            if t <= h:
                end = mid
            else:
                start = mid

        return mink


