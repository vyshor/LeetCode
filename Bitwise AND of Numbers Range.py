class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        lower, upper = left, right
        count = 0
        while lower != upper:
            lower >>= 1
            upper >>= 1
            count += 1

        return lower << count

# 2: 0010
# 4: 0100

# 5: 0101
# 6: 0110
# 7: 0111
# 8: 1000
