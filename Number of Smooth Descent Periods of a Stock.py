class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        left, right = 0, 0
        count = 0

        while right < n:
            # print(count, prices[right])
            if right == 0 or prices[right]+1 == prices[right-1]:
                count += right - left + 1
                right += 1
            else:
                left = right
                right += 1
                count += 1

        return count
