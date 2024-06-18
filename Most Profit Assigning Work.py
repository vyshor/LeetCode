class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        q = []
        n = len(profit)
        min_difficulty = float('inf')
        max_profit = 0
        for i in range(n):
            min_difficulty = min(min_difficulty, difficulty[i])
            max_profit = max(max_profit, profit[i])
            q.append([difficulty[i], -profit[i]])

        q.sort()
        maxx = 0
        for i in range(n):
            maxx = min(maxx, q[i][1])
            q[i][1] = maxx

        # print(q)
        total = 0
        for w in worker:
            if w < min_difficulty:
                continue

            i = bisect.bisect_left(q, [w, -max_profit])
            # print(i)
            if i < n and w == q[i][0]:
                total -= q[i][1]
            else:
                total -= q[i - 1][1]
        return total
