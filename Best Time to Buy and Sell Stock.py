class Solution:
    # Need one starting point that is local minimum, starting < prev & starting < next
    # Then find next point that have to be local maximum, next > starting & next > next->next
    # Added profits = next - starting
    def maxProfit(self, prices: List[int]) -> int:
        buy = True
        prev = 999
        profits = 0
        buy_p = 0
        i = 0
        n = len(prices)
        while i < n:
            cur = prices[i]
            if buy:
                try:
                    next = prices[i + 1]
                    if cur < prev and cur < next:
                        buy = False
                        buy_p = cur
                except IndexError:
                    pass
            else:
                try:
                    next = prices[i + 1]
                    if cur > prev and cur > next:
                        buy = True
                        profits += cur - buy_p
                        buy_p = 0
                except IndexError:
                    profits += cur - buy_p
            prev = cur
            i += 1
        return profits


class Solution:
    # Need one starting point that is local minimum, starting < prev & starting < next
    # Then find next point that have to be local maximum, next > starting & next > next->next
    # Added profits = next - starting
    def maxProfit(self, prices: List[int]) -> int:
        prev = 999
        profits = []
        buy_p = 0
        i = 0
        n = len(prices)
        while i < n:
            cur = prices[i]
            try:
                next = prices[i + 1]
                if cur <= prev and cur < next:
                    buy = False
                    profits.append(max(prices[i + 1:]) - cur)
            except IndexError:
                pass
            prev = cur
            i += 1
        if profits:
            return max(profits)
        else:
            return 0

# O(n^3)
# O(n) for iterating through each item
# O(n) for finding max in remaining stuf
# O(n) for finding max in all the profits

# Runtime: 80 ms, faster than 27.85% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.8 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.

# 