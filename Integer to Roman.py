class Solution:
    def intToRoman(self, num: int) -> str:
        dp = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        ans = ''
        for div, letter in dp.items():
            count = (num // div)
            ans += letter * count
            num = num - count*div
        return ans

# Time: O(n)
# Space: O(1)

# Runtime: 44 ms, faster than 87.75% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.2 MB, less than 86.07% of Python3 online submissions for Integer to Roman.

