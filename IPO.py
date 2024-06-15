class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        q = []
        q2 = []
        for i in range(n):
            if w >= capital[i]:
                q.append(-profits[i])
            else:
                q2.append((capital[i], profits[i]))

        heapq.heapify(q)
        heapq.heapify(q2)

        if not q:
            return w

        w -= heapq.heappop(q)
        k -= 1

        while k > 0:
            while q2 and q2[0][0] <= w:
                _, p = heapq.heappop(q2)
                heapq.heappush(q, -p)

            if not q:
                break

            w -= heapq.heappop(q)
            k -= 1
        return w
