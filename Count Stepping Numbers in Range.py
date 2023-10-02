class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        n = len(high)
        m = len(low)
        lo, hi = ['0'] * (n - m) + list(low), list(high)

        leading = n - m
        path = ['0'] * leading
        count = 0
        dp = {}

        def calculateComb(currentDigit, digitsLeft):
            if (currentDigit, digitsLeft) in dp:
                return dp[(currentDigit, digitsLeft)]

            if digitsLeft == 0:
                dp[(currentDigit, digitsLeft)] = 1
                return 1

            if currentDigit == "9":
                result = calculateComb("8", digitsLeft - 1)
                dp[(currentDigit, digitsLeft)] = result
                return result

            if currentDigit == "0":
                result = calculateComb("1", digitsLeft - 1)
                dp[(currentDigit, digitsLeft)] = result
                return result

            num = int(currentDigit)
            result = calculateComb(str(num + 1), digitsLeft - 1) + calculateComb(str(num - 1), digitsLeft - 1)
            dp[(currentDigit, digitsLeft)] = result
            return result

        def compare(arrA, arrB):
            a, b = len(arrA), len(arrB)
            m = min(a, b)
            for i in range(m):
                if arrA[i] < arrB[i]:
                    return -1
                elif arrB[i] < arrA[i]:
                    return 1
            return 0

        def explorePath():
            nonlocal path, n, lo, hi, count
            # print(lo, hi, path)
            # print("Count", count)

            lo_path = compare(lo, path)
            path_hi = compare(path, hi)
            if lo_path == -1 and path_hi == -1:
                count += calculateComb(path[-1], n - len(path))
                return

            if lo_path == 1 or path_hi == 1:
                return

            if len(path) == n:
                count += 1
                return

            last = int(path[-1])
            for next in [last + 1, last - 1]:
                if 0 <= next <= 9:
                    path.append(str(next))
                    explorePath()
                    path.pop()

        while leading >= 0:
            # print(leading)
            for i in range(1, 10):
                path.append(str(i))
                explorePath()
                path.pop()

            leading -= 1
            if leading >= 0:
                path.pop()

        return count % (10 ** 9 + 7)
