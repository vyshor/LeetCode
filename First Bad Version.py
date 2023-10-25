# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        minn = right

        while left < right + 1:
            mid = (left + right) // 2
            bad = isBadVersion(mid)
            if bad:
                minn = min(minn, mid)
                right = mid - 1
            else:
                left = mid + 1

        return minn
