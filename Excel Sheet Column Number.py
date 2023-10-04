class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        num = 0
        factor = 0
        for i in range(n-1, -1, -1):
            num += (ord(columnTitle[i])-64)*(26**factor)
            factor += 1
        return num
