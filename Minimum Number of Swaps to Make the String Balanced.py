class Solution:
    def minSwaps(self, s: str) -> int:
        n = 0
        count = 0
        for c in s:
            if c == '[':
                n += 1
            else:
                if n == 0:
                    count += 1
                    n += 1
                else:
                    n -= 1
        return count
