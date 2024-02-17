class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        diffs = [[0, 0]]

        h = heights[0]
        for i in range(1, n):
            if heights[i] > h:
                diffs.append([heights[i] - h, i])
            else:
                diffs[-1][1] = i
            h = heights[i]

        if ladders >= len(diffs) - 1:
            return n - 1

        q = []
        m = len(diffs)
        pos = diffs[ladders][1]
        for i in range(1, ladders + 1):
            heapq.heappush(q, diffs[i][0])

        i = ladders + 1
        while i < m:
            diff, new_pos = diffs[i]
            heapq.heappush(q, diff)
            bricks -= heapq.heappop(q)
            if bricks < 0:
                return pos
            else:
                pos = new_pos
                i += 1
        return pos

