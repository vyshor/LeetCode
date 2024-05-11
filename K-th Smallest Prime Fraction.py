class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = []
        for i in range(n):
            for j in range(i+1, n):
                heapq.heappush(q, (-arr[i]/arr[j], arr[i], arr[j]))

                if len(q) > k:
                    heapq.heappop(q)
        return [q[0][1], q[0][2]]
