class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t0 = 0
        total = 0
        for (a, t) in customers:
            if t0 <= a:
                total += t
                t0 = a+t
            else:
                total += (t0-a) + t
                t0 = t0+t
        return total / len(customers)
