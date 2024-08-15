class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c0, c1 = 0, 0
        for bill in bills:
            if bill == 5:
                c0 += 1
            elif bill == 10:
                if c0 == 0:
                    return False
                c0 -= 1
                c1 += 1
            else:
                if c1 >= 1 and c0 > 0:
                    c1 -= 1
                    c0 -= 1
                elif c0 >= 3:
                    c0 -= 3
                else:
                    return False
        return True
