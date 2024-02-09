class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        d = (a | b)
        count = 0
        maxx = max(d, c)
        while maxx:
            if (d % 2) != (c % 2):
                if c % 2 == 0:
                    count += (a % 2 + b % 2)
                else:
                    count += 1

            a >>= 1
            b >>= 1
            c >>= 1
            d >>= 1
            maxx >>= 1

        return count
