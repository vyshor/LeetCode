class Solution:
    def myAtoi(self, s: str) -> int:
        n = ''
        for c in s.strip():
            if c.isdigit():
                n += c
            elif n == "":
                if c == "-":
                    n = '-'
                elif c == "+":
                    n = '+'
                else:
                    break
            else:
                break
        if not n or n == "-" or n == "+":
            return 0
        return max(min(int(n),  2**31 -1),-2**31)
