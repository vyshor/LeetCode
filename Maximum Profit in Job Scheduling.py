class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        q = []
        n = len(profit)
        for i in range(n):
            q.append((startTime[i], endTime[i], True, profit[i]))

        heapq.heapify(q)
        total = 0
        while q:
            start, end, isJob, earn = heapq.heappop(q)
            if isJob:
                heapq.heappush(q, (end, 0, False, total + earn))
            else:
                total = max(total, earn)

        return total

