class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        num = ""
        digits = set()
        for c in word:
            if c.isalpha():
                if num:
                    digits.add(int(num))
                    num = ""
            else:
                num += c

        if num:
            digits.add(int(num))

        return len(digits)
