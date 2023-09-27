class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        prev = -1
        maxx = 1
        for i, seated in enumerate(seats):
            if seated:
                if prev == -1:
                    maxx = max(maxx, i)
                else:
                    maxx = max(maxx, (i-prev)//2)
                prev = i
        maxx = max(maxx, n-prev-1)
        return maxx
