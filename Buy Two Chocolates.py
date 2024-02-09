class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        summ = heapq.heappop(prices) + prices[0]
        if summ > money:
            return money
        return money - summ
