class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        if n == 1:
            return 10

        prev = 10
        for j in range(2, n + 1):
            count = 9
            for i in range(9, 10 - j, -1):
                count *= i
            prev += count

        return prev
