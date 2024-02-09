class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na, nb = len(a), len(b)
        i = na - 1
        j = nb - 1

        ans = []
        carry_over = 0
        while i >= 0 or j >= 0:
            summ = carry_over

            if i >= 0:
                summ += int(a[i])
                i -= 1

            if j >= 0:
                summ += int(b[j])
                j -= 1

            carry_over = summ // 2
            summ %= 2

            ans.append(str(summ))

        if carry_over:
            ans.append(str(carry_over))

        return ''.join(reversed(ans))


