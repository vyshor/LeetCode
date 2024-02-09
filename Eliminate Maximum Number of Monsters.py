class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time = []
        for i in range(n):
            t = dist[i] / speed[i]
            time.append(t)

        time.sort()

        j = 1
        for i in range(1, n):
            if time[i] <= j:
                return j
            j += 1

        return j
