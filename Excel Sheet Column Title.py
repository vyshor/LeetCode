class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber > 0:
            if columnNumber <= 26:
                s = chr(columnNumber + 64) + s
                return s

            d = columnNumber % 26
            columnNumber = columnNumber // 26

            if d == 0:
                s = "Z" + s
                columnNumber -= 1
            else:
                s = chr(d + 64) + s
        return s
