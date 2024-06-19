class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n // k < m:
            return -1

        def check(day):
            nonlocal n, k
            bouquet = 0
            streak = 0
            for i in range(n):
                if bloomDay[i] <= day:
                    streak += 1
                    if streak == k:
                        bouquet += 1
                        streak = 0
                        if bouquet == m:
                            return True
                else:
                    streak = 0
            return False

        left, right = min(bloomDay), max(bloomDay)
        minn = right
        while left < right:
            mid = (left + right) // 2
            # print(left, right, minn, mid, check(mid))
            if check(mid):
                right = mid
                minn = min(minn, mid)
            else:
                if mid == left:
                    break
                left = mid
        return minn
