class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        prev = points[0][0] - 1
        count = 0
        for (start, end) in points:
            if prev >= start:
                continue
            else:
                count += 1
                prev = end

        return count
