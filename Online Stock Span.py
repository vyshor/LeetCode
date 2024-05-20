class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        total = 1
        while self.arr and self.arr[-1][0] <= price:
            total += self.arr[-1][1]
            self.arr.pop()

        self.arr.append((price, total))
        return total

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
