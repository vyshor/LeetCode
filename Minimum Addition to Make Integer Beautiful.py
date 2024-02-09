class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        summ = 0
        digits = [0]
        for c in str(n):
            digit = int(c)
            digits.append(digit)
            summ += digit

        if summ <= target:
            return 0

        n = len(digits)

        def increaseDigit(i, delta):
            nonlocal digits, summ
            prev = digits[i]
            digits[i] += delta

            if digits[i] >= 10:
                digits[i] %= 10
                increaseDigit(i - 1, 1)

            summ += digits[i] - prev

        minn = 0
        factor = 1
        j = 1
        while summ > target:
            i = n - j
            digit = digits[i]
            if digit != 0:
                delta = 10 - digit
                increaseDigit(i, delta)
                minn += delta * factor

            factor *= 10
            j += 1

        return minn


