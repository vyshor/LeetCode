class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        ratio = []
        for i in range(n):
            ratio.append((wage[i]/quality[i], quality[i]))
        ratio.sort()
        rate = ratio[k-1][0]
        q = [-qty for _, qty in ratio[:k]]
        total = -sum(q)
        minn = rate * total
        heapq.heapify(q)
        for i in range(k, n):
            rate = ratio[i][0]
            heapq.heappush(q, -ratio[i][1])
            total += ratio[i][1] + heapq.heappop(q)
            minn = min(minn, rate*total)
        return minn
