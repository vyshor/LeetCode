class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        dp = set()
        i = 1
        while True:
            sq = i*i
            if sq == c:
                return True
            if sq > c:
                break
            dp.add(sq)
            if c-sq in dp:
                return True
            i += 1
        return False
