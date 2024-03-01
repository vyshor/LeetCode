class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        count = 0
        for i in range(n):
            if s[i] == '1':
                count += 1

        num = []
        for i in range(n - 1):
            if count > 1:
                num.append("1")
                count -= 1
            else:
                num.append("0")

        num.append("1")
        return ''.join(num)
