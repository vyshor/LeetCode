class Solution:
    def fractionAddition(self, expression: str) -> str:
        n = len(expression)
        i = 0
        numerator = ''
        denominator = ''
        num = []
        den = []
        look_num = True
        pos = True
        while i < n:
            c = expression[i]
            if c == '+' or c == '-':
                if numerator:
                    num.append(int(numerator) * (-1 if not pos else 1))
                    numerator = ''
                else:
                    num.append(0)

                if denominator:
                    den.append(int(denominator))
                    denominator = ''
                else:
                    den.append(1)

                pos = (c == '+')
                look_num = True
            elif c == "/":
                look_num = False
            elif look_num:
                numerator += c
            else:
                denominator += c
            i += 1

        num.append(int(numerator) * (-1 if not pos else 1))
        den.append(int(denominator))
        # print(num)
        # print(den)
        n = len(num)
        product = 1
        for d in den:
            if product % d == 0:
                continue
            product *= d

        summ = 0
        for i in range(n):
            summ += num[i] * (product // den[i])

        while summ % 2 == 0 and product % 2 == 0:
            summ //= 2
            product //= 2

        # print(summ, product)
        sign = summ < 0
        summ = abs(summ)
        j = 3
        while j <= summ and j <= product and summ > 1 and product > 1:
            if summ % j == 0 and product % j == 0:
                summ //= j
                product //= j
            else:
                j += 2
        return str(summ * (-1 if sign else 1)) + "/" + str(product)
