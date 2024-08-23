class Solution:
    def findComplement(self, num: int) -> int:
        i = 0
        ans = 0
        while num:
            if num % 2 == 0:
                ans |= (1 << i)
            i += 1
            num >>= 1
        return ans
