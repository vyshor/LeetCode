class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ''
        for num in range(numRows):
            row = ''
            pt = num
            i = 1
            while pt < len(s):
                row += s[pt]
                reflect_index = ((numRows - 1)*2)*i - num
                if pt % ((numRows - 1)*2) and pt % ((numRows - 1)*2) != numRows - 1 and reflect_index < len(s):
                    row += s[reflect_index]
                pt += ((numRows - 1)*2)
                i += 1
            ans += row
        return ans

# Time: O(n)
# Space: O(n)

# Runtime: 76 ms, faster than 31.17% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 14.3 MB, less than 71.41% of Python3 online submissions for ZigZag Conversion.