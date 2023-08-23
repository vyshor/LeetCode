class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        dp = [x]
        bit = []
        negative = n < 0

        if negative:
            n *= -1

        i = n
        while i > 1:
            bit.append(i % 2)
            i = i // 2
            dp.append(0)
        bit.append(1)

        summ = float(1)
        size = len(dp)
        for i in range(1, size):
            dp[i] = dp[i - 1] * dp[i - 1]
            if bit[i]:
                summ *= dp[i]

        if bit[0]:
            summ *= dp[0]

        # print(summ)
        # print(1/summ)
        # print(dp)
        # print(bit)

        if negative:
            return 1 / summ

        return summ
