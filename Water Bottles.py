class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        remainder = 0
        while numBottles:
            count += numBottles
            numBottles += remainder
            remainder = numBottles % numExchange
            numBottles //= numExchange
        return count
