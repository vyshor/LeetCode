class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n == 1:
            return 0

        if n == 2:
            return 1

        stockPrices.sort()
        count = 1
        prev = stockPrices[0]

        for i in range(2, n):
            (x, y) = prev
            (x1, y1) = stockPrices[i]
            (x2, y2) = stockPrices[i - 1]

            if (y2 - y) * (x1 - x) != (y1 - y) * (x2 - x):
                count += 1

            prev = stockPrices[i - 1]

        return count
