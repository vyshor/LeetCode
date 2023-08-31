class Solution:
    def calculateGradient(self, ptA, ptB):
        x1, y1 = ptA
        x2, y2 = ptB

        if x1 == x2:
            return float('inf')

        return (y1 - y2) / (x1 - x2)

    def calculateIntercept(self, ptA, grad):
        x1, y1 = ptA
        if grad == float('inf'):
            return x1

        return y1 - grad * x1

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dp = {}
        maxx = 1

        for ptA in points:
            for ptB in points:
                ptA = tuple(ptA)
                ptB = tuple(ptB)

                if ptA == ptB:
                    continue

                grad = self.calculateGradient(ptA, ptB)
                intercept = self.calculateIntercept(ptA, grad)

                if (grad, intercept) not in dp:
                    dp[(grad, intercept)] = {ptA, ptB}
                    maxx = max(maxx, 2)
                else:
                    dp[(grad, intercept)].add(ptA)
                    dp[(grad, intercept)].add(ptB)
                    maxx = max(maxx, len(dp[(grad, intercept)]))

        # print(dp)

        return maxx
