import math

def totalTime(dist, spd):
    t = 0
    for d in dist[:-1]:
        t += math.ceil(d / spd)
    t += dist[-1] / spd
    return t

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        minn, maxx = 1, 10_000_001
        minSpeed = -1
        while minn < maxx:
            mid = (minn + maxx) // 2
            t = totalTime(dist, mid)
            if t <= hour:
                if minSpeed == -1 or mid < minSpeed:
                    minSpeed = mid
                    maxx = mid
                    continue

            if mid == minn:
                break

            minn = mid
        return minSpeed

