class Solution:
    def totalMoney(self, n: int) -> int:
        mondays = n // 7 + 1
        summ = mondays * 28 + (7 * (mondays * (mondays - 1)) // 2)
        remainder = n % 7 + 1
        # print(mondays, summ, remainder)
        for i in range(remainder, 8):
            summ -= i + (mondays - 1)
        return summ
