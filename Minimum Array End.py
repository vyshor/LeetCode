class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = 0
        n -= 1
        i = 0
        shift = 0
        while n or x:
            # print(n, x, ans)
            if x & 1:
                shift = 1
            else:
                shift = (n & 1)
                n >>= 1

            ans |= (shift << i)
            x >>= 1
            i += 1
        return ans
